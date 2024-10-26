from django.shortcuts import render, redirect
import random

# List of questions and answers
questions = [
    {"question": "What does CPU stand for?", "answer": "central processing unit"},
    {"question": "What does GPU stand for?", "answer": "graphics processing unit"},
    {"question": "What does RAM stand for?", "answer": "random access memory"},
    {"question": "What does PSU stand for?", "answer": "power supply unit"},
    {"question": "What does SSD stand for?", "answer": "solid state drive"},
    {"question": "What does HDD stand for?", "answer": "hard disk drive"},
    {"question": "What is the main function of the operating system?", "answer": "manage hardware and software resources"},
    {"question": "Which company developed the Windows OS?", "answer": "microsoft"},
    {"question": "Which programming language is known as the language of the web?", "answer": "javascript"},
    {"question": "What does HTTP stand for?", "answer": "hypertext transfer protocol"},
]

def welcome_view(request):
    if request.method == 'POST':
        return redirect('quiz_view')
    return render(request, 'welcome.html')

def quiz_view(request):
    if request.method == 'POST':
        # Handle form submission
        user_answers = []
        for i in range(len(questions)):
            user_answer = request.POST.get(f'question-{i}')
            user_answers.append(user_answer)

        # Calculate score
        score = 0
        for i, answer in enumerate(user_answers):
            if answer and answer.lower() == questions[i]['answer']:
                score += 1

        total_questions = len(questions)
        return redirect('quiz:results', score=score, total=total_questions)

    return render(request, 'quiz.html', {'questions': questions[:5]})

def results_view(request, score, total):
    # Calculate the percentage score
    percentage_score = (score / total) * 100 if total > 0 else 0
    return render(request, 'results.html', {'score': score, 'total': total, 'percentage_score': percentage_score})
