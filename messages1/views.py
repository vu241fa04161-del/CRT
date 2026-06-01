from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Quiz, Question, Result, Student


def base(request):
    return render(request, "quiz/base.html")


def home(request):
    return render(request, "quiz/home.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        Student.objects.create(
            user=user,
            name=username,
            email=email
        )

        messages.success(request, "Registration Successful")
        return redirect("login")

    return render(request, "quiz/register.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(
                request,
                "Invalid Username or Password"
            )
            return redirect("login")

    return render(request, "quiz/login.html")


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "quiz/dashboard.html")


def list(request):
    quizzes = Quiz.objects.all()
    return render(request, "quiz/list.html", {'quizzes': quizzes})


def time(request):
    return render(request, "quiz/time.html")


def result(request):
    return render(request, "quiz/result.html")


def resulthistory(request):
    if not request.user.is_authenticated:
        return redirect("login")
    results = Result.objects.filter(student=request.user).order_by('-date_taken')
    return render(
        request,
        "quiz/resulthistory.html",
        {'results': results}
    )


def leaderboard(request):
    results = Result.objects.all().order_by('-score')
    return render(
        request,
        "quiz/leaderboard.html",
        {'results': results}
    )


def multiple_quizess(request):
    return render(request, "quiz/multiple_quizess.html")


def forgetpassword(request):
    return render(request, "quiz/forgetpassword.html")


def logout_view(request):
    logout(request)
    return redirect("login")


def quizess(request):
    quizzes = Quiz.objects.all()
    return render(
        request,
        'quiz/quizess.html',
        {'quizess': quizzes} # Template expects 'quizess' key
    )


def quiz_detail(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "Please log in first to write the quiz!")
        return redirect("login")

    quiz = get_object_or_404(Quiz, id=id)
    questions = Question.objects.filter(quiz=quiz)

    if request.method == "POST":
        score = 0
        total = questions.count()

        for question in questions:
            # HTML radio button name is question.id (converted to string)
            selected_option = request.POST.get(str(question.id))
            if selected_option and selected_option == question.correct_answer:
                score += 1

        if request.user.is_authenticated:
            Result.objects.create(
                student=request.user,
                quiz=quiz,
                score=score,
                total=total
            )

        percentage = round((score / total) * 100) if total > 0 else 0
        return render(
            request,
            'quiz/result.html',
            {
                'quiz': quiz,
                'score': score,
                'total': total,
                'percentage': percentage
            }
        )

    return render(
        request,
        'quiz/quiz_detail.html',
        {
            'quiz': quiz,
            'questions': questions
        }
    )



