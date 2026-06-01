from django.db import models
from django.contrib.auth.models import User

# =========================
# Student Model
# =========================
class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=100
    )
    email = models.EmailField(
        unique=True
    )

    def __str__(self):
        return self.name


# =========================
# Quiz Model
# =========================
class Quiz(models.Model):
    LEVEL_CHOICES = (
        ('Simple', 'Simple'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )

    title = models.CharField(
        max_length=200
    )
    description = models.TextField()
    category = models.CharField(
        max_length=100,
        default="General"
    )
    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default="Simple"
    )
    time_limit = models.IntegerField(
        default=20,
        help_text="Time in minutes"
    )

    def __str__(self):
        return f"{self.title} ({self.level})"


# =========================
# Question Model
# =========================
class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    question = models.TextField()
    option1 = models.CharField(
        max_length=200
    )
    option2 = models.CharField(
        max_length=200
    )
    option3 = models.CharField(
        max_length=200
    )
    option4 = models.CharField(
        max_length=200
    )
    correct_answer = models.CharField(
        max_length=200,
        default=""
    )
    marks = models.IntegerField(
        default=1
    )

    def __str__(self):
        return self.question


# =========================
# Result Model
# =========================
class Result(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE
    )
    score = models.IntegerField()
    total = models.IntegerField()
    date_taken = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student.username} - {self.quiz.title}"