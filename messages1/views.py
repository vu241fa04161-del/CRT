import json
import os
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def ai_guidance(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST requests are allowed"}, status=400)
    
    try:
        data = json.loads(request.body)
        message = data.get("message", "").strip()
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    if not message:
        return JsonResponse({"response": "🤖 Beep boop! Please say something!"})

    # 1. Cheat check
    cheat_keywords = [
        "answer", "correct option", "solve this", "solution", "which is correct",
        "give me the key", "correct answer", "solve question", "what is the option",
        "cheat", "exam help", "tell me the answer of", "what is the answer"
    ]
    message_lower = message.lower()
    if any(kw in message_lower for kw in cheat_keywords):
        return JsonResponse({
            "response": "🤖 **Beep Boop! Proctor Warning!**\n\nI am programmed to help you learn and adopt **eco-friendly habits**, as well as guide you about the features of this **Quiz Portal**!\n\n❌ **I am strictly forbidden from giving quiz answers or helping you cheat.** To test your real skills, please read the questions carefully and try to solve them on your own! You've got this! 🌟"
        })

    # 2. Check if Gemini API key exists
    gemini_key = os.environ.get("GEMINI_API_KEY")
    if gemini_key:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={gemini_key}"
            headers = {"Content-Type": "application/json"}
            payload = {
                "contents": [
                    {
                        "role": "user",
                        "parts": [{"text": message}]
                    }
                ],
                "systemInstruction": {
                    "parts": [
                        {
                            "text": (
                                "You are a friendly AI Robot Mentor and Eco-Advisor for our Quiz Portal app. "
                                "Your goals are:\n"
                                "1. Guide users on how to be eco-friendly. Focus on digital sustainability (e.g. using dark mode to save energy, shutting down idle computers, deleting unused cloud data/emails, eco-friendly physical habits, reducing e-waste, recycling electronics).\n"
                                "2. Explain the features and structure of this Quiz Portal app. We offer beautiful glassmorphic quizzes in HTML, CSS, JavaScript, Python, and Django, as well as leaderboards, dashboard tracking, and history logs.\n"
                                "3. CRITICAL: NEVER give answers, solutions, correct options, or code blocks that solve specific quiz questions! If the user asks for quiz answers or tries to cheat, you must strictly and politely decline. Tell them you are here to teach them about green habits and our app features, not to solve the exam for them!\n"
                                "Keep your answers friendly, robotic, interactive, clean, structured, and use emojis."
                            )
                        }
                    ]
                },
                "generationConfig": {
                    "maxOutputTokens": 450,
                    "temperature": 0.7
                }
            }
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            if response.status_code == 200:
                res_data = response.json()
                bot_text = res_data['candidates'][0]['content']['parts'][0]['text']
                return JsonResponse({"response": bot_text})
        except Exception as e:
            pass # Fall back to rule-based engine on any error

    # 3. Fallback Engine (Robotic, helpful, eco-focused)
    eco_keywords = ["eco", "green", "carbon", "environment", "nature", "earth", "save", "power", "energy", "planet", "recycle", "sustainable"]
    app_keywords = ["app", "quiz", "portal", "play", "features", "how", "what is", "about", "leaderboard", "history", "dashboard"]

    if any(kw in message_lower for kw in eco_keywords):
        fallback_res = (
            "🤖 **Beep Boop! Eco-Advisor Protocol Activated!** 🌿\n\n"
            "I'd love to help you protect our planet! Here are some excellent digital and physical eco-friendly practices:\n\n"
            "• 🔋 **Use Dark Mode**: Darker themes consume less power on modern displays. Our Quiz Portal features a premium dark theme to help reduce energy consumption!\n"
            "• 📧 **Digital Spring Cleaning**: Delete old emails, messages, and unused cloud files. Reducing data center storage demands saves massive amounts of electricity globally!\n"
            "• 🔌 **Power Off**: Fully shut down your devices when done. Putting them on sleep mode still draws 'phantom' standby power.\n"
            "• ♻️ **Recycle E-waste**: Don't throw old phones or laptops in the trash. Dispose of them at certified e-waste facilities so valuable materials can be recycled.\n\n"
            "What other green tips would you like to explore? 🌎"
        )
    elif any(kw in message_lower for kw in app_keywords):
        fallback_res = (
            "🤖 **Affirmative! Accessing Quiz Portal Database...** ⚡\n\n"
            "Here is a complete breakdown of our application features:\n\n"
            "• 📝 **Quizzes**: We offer customizable real-time quizzes covering HTML5, CSS Flexbox, JavaScript ES6, Python, and Django.\n"
            "• ⏱️ **Timer**: Every quiz has an elegant floating real-time countdown timer to help you build speed!\n"
            "• 🏆 **Leaderboard**: Compete with other learners globally and view rank updates in real-time.\n"
            "• 📊 **History & Dashboard**: View your past scores, percentages, and performance graphs to track your learning journey.\n"
            "• 🌐 **Multilingual**: Switch languages easily using the top bar dropdown.\n\n"
            "Head to the **Quizzes** tab in the navbar to start a challenge! 🚀"
        )
    else:
        fallback_res = (
            "🤖 **Greetings, human! I am your AI Robot Mentor!** 🤖\n\n"
            "I am programmed to guide you through the **Quiz Portal** and help you develop **eco-friendly digital habits**! 🌿\n\n"
            "Ask me things like:\n"
            "• *'How can I save energy?'*\n"
            "• *'Tell me about the app features!'*\n\n"
            "*(Remember, I cannot help with quiz answers to keep the leaderboard fair and fun!)*"
        )

    return JsonResponse({"response": fallback_res})



