from django.contrib import admin
from django.urls import path, include
from messages1 import views as m_v
from messages1.models import Quiz
urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include('messages1.api_urls')),

    path('base/', m_v.base, name='base'),

    path('', m_v.home, name='home'),

    path('register/', m_v.register, name='register'),

    path('login/', m_v.user_login, name='login'),

    path('dashboard/', m_v.dashboard, name='dashboard'),

    path('list/', m_v.list, name='list'),

    path('time/', m_v.time, name='time'),

    path('result/', m_v.result, name='result'),

    path(
        'resulthistory/',
        m_v.resulthistory,
        name='resulthistory'
    ),

    path(
        'leaderboard/',
        m_v.leaderboard,
        name='leaderboard'
    ),

    path(
        'multiple_quizess/',
        m_v.multiple_quizess,
        name='multiple_quizess'
    ),

    path(
    'quizess/',
    m_v.quizess,
    name='quizess'
),

    path(
        'forgetpassword/',
        m_v.forgetpassword,
        name='forgetpassword'
    ),
    

  path('ai-guidance/', m_v.ai_guidance, name='ai_guidance'),
  path('logout/', m_v.logout_view, name='logout'),
  path(
        'quiz/<int:id>/',
        m_v.quiz_detail,
        name='quiz_detail'
    ),

]