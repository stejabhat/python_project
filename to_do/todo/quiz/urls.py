from django.urls import path
from .views import welcome_view, quiz_view, results_view

app_name = 'quiz'

urlpatterns = [
    path('', welcome_view, name='welcome'),  # Welcome page
    path('quiz/', quiz_view, name='quiz'),    # Quiz page
    path('results/<int:score>/<int:total>/', results_view, name='results'),  # Results page
]
