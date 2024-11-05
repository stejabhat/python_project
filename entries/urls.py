from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
     path('login/', CustomLoginView.as_view(), name='login'),  # Use Django's LoginView
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Use Django's LogoutView
    path('entries/', views.entry_list, name='entry_list'),
    path('entries/add/', views.add_entry, name='add_entry'),
    path('entries/<int:entry_id>/', views.entry_detail, name='entry_detail'),
    path('entries/<int:entry_id>/edit/', views.edit_entry, name='edit_entry'),
    path('entries/<int:entry_id>/delete/', views.delete_entry, name='delete_entry'),
    path('entries/<int:entry_id>/toggle_publish/', views.toggle_publish, name='toggle_publish'), 
    path('my-entries/', views.my_entries, name='my_entries'),
    path('logout/', views.custom_logout, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
