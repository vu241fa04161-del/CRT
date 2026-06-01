from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Quiz, Question, Result, Student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Create Student profile
        Student.objects.create(
            user=user,
            name=validated_data['username'],
            email=validated_data['email']
        )
        return user

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'category', 'level', 'time_limit']

class QuestionSerializer(serializers.ModelSerializer):
    # We do NOT include correct_answer here to prevent cheating
    class Meta:
        model = Question
        fields = ['id', 'question', 'option1', 'option2', 'option3', 'option4', 'marks']

class QuizDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'category', 'level', 'time_limit', 'questions']

class ResultSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.username', read_only=True)
    quiz_title = serializers.CharField(source='quiz.title', read_only=True)

    class Meta:
        model = Result
        fields = ['id', 'student', 'quiz_title', 'score', 'total', 'date_taken']
