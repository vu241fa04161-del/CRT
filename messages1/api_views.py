from rest_framework import status, viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Quiz, Question, Result
from .serializers import (
    UserSerializer,
    UserRegisterSerializer,
    QuizSerializer,
    QuizDetailSerializer,
    ResultSerializer
)

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response(
                {'error': 'Please provide both username and password'},
                status=status.HTTP_400_BAD_REQUEST
            )
        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': UserSerializer(user).data
        }, status=status.HTTP_200_OK)

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(
            {'message': 'Logged out successfully'},
            status=status.HTTP_200_OK
        )

class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuizDetailSerializer
        return QuizSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def submit(self, request, pk=None):
        quiz = self.get_object()
        questions = Question.objects.filter(quiz=quiz)
        
        raw_answers = request.data.get('answers', {})
        answers_dict = {}
        
        # Support both {"1": "option", "2": "option"} and [{"question_id": 1, "selected_option": "option"}]
        if isinstance(raw_answers, list):
            for item in raw_answers:
                if isinstance(item, dict) and 'question_id' in item:
                    answers_dict[str(item['question_id'])] = item.get('selected_option', '')
        elif isinstance(raw_answers, dict):
            answers_dict = {str(k): v for k, v in raw_answers.items()}
        
        score = 0
        total = questions.count()
        
        for q in questions:
            user_ans = answers_dict.get(str(q.id))
            if user_ans and user_ans == q.correct_answer:
                score += 1
                
        result = Result.objects.create(
            student=request.user,
            quiz=quiz,
            score=score,
            total=total
        )
        
        percentage = round((score / total) * 100) if total > 0 else 0
        
        return Response({
            'score': score,
            'total': total,
            'percentage': percentage,
            'result_id': result.id
        }, status=status.HTTP_201_CREATED)

class LeaderboardAPIView(generics.ListAPIView):
    queryset = Result.objects.all().order_by('-score', '-date_taken')
    serializer_class = ResultSerializer
    permission_classes = [AllowAny]

class ResultHistoryAPIView(generics.ListAPIView):
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Result.objects.filter(student=self.request.user).order_by('-date_taken')
