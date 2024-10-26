from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('chatbot/logout/', views.login, name='logout'),
    path('main/',views.main, name = 'main'),
    path('contact/',views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
]
# myproject/urls.py