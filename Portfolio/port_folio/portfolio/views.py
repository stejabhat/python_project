from django.shortcuts import render

def portfolio(request):
    return render(request, 'portfolio.html')
# views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

def resume_view(request):
    file_path = os.path.join(settings.BASE_DIR, 'static', 'resume', 'Resume_Teja_Bhat.pdf')
    if not os.path.exists(file_path):
        return HttpResponse("File not found", status=404)
    with open(file_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Resume_Teja_Bhat.pdf"'
        return response