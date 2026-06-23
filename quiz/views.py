from django.shortcuts import render
from .models import Question, Score

def user_login(request):
    # For now, just show a simple login page
    return render(request, 'quiz/user_login.html')

def portal_view(request):
    # This will render the portal page template
    return render(request, 'quiz/portal.html')

def quiz_view(request):
    questions = Question.objects.all()
    return render(request, 'quiz/quiz.html', {'questions': questions})

def result_view(request):
    questions = Question.objects.all()
    score = 0
    for q in questions:
        selected = request.POST.get(str(q.id))
        if selected and int(selected) == q.correct_option:
            score += 1
    user = request.POST.get("username", "Anonymous")
    Score.objects.create(user=user, score=score)
    return render(request, 'quiz/result.html', {'score': score, 'total': len(questions)})





