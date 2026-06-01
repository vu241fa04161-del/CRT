from django.urls import path
from .api_views import (
    RegisterAPIView,
    LoginAPIView,
    LogoutAPIView,
    QuizViewSet,
    LeaderboardAPIView,
    ResultHistoryAPIView
)

urlpatterns = [
    # Authentication
    path('auth/register/', RegisterAPIView.as_view(), name='api_register'),
    path('auth/login/', LoginAPIView.as_view(), name='api_login'),
    path('auth/logout/', LogoutAPIView.as_view(), name='api_logout'),

    # Quizzes
    path('quizzes/', QuizViewSet.as_view({'get': 'list'}), name='api_quiz_list'),
    path('quizzes/<int:pk>/', QuizViewSet.as_view({'get': 'retrieve'}), name='api_quiz_detail'),
    path('quizzes/<int:pk>/submit/', QuizViewSet.as_view({'post': 'submit'}), name='api_quiz_submit'),

    # Leaderboard & History
    path('leaderboard/', LeaderboardAPIView.as_view(), name='api_leaderboard'),
    path('results/', ResultHistoryAPIView.as_view(), name='api_results'),
]
