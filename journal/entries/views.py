from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Entry
from .forms import EntryForm

# Main page
def index(request):
    # Display only published entries for the index page
    entries = Entry.objects.filter(published=True).order_by('-created_at')
    return render(request, 'index.html', {'entries': entries})

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('entry_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('entry_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)
    return redirect('index')

# Entry list view
@login_required
def entry_list(request):
    entries = Entry.objects.filter(user=request.user, published=True).order_by('-created_at')
    return render(request, 'entry_list.html', {'entries': entries})



# Add new entry view
@login_required
def add_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.published = request.POST.get('published') == 'true'
            entry.save()
            return redirect('index')
    else:
        form = EntryForm()
    return render(request, 'add_entry.html', {'form': form})


# Edit entry view
@login_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id, user=request.user)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_list')
    else:
        form = EntryForm(instance=entry)
    return render(request, 'edit_entry.html', {'form': form})

# Delete entry view
@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id, user=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('entry_list')
    return render(request, 'entry_list.html')

# Entry detail view
@login_required
def entry_detail(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id, user=request.user)
    return render(request, 'entry_detail.html', {'entry': entry})
@login_required
def toggle_publish(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id, user=request.user)
    entry.published = not entry.published  # Toggle the published status
    entry.save()
    return redirect('entry_list')

@login_required
def my_entries(request):
    # Display all entries (published and drafts) for the logged-in user
    entries = Entry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_entries.html', {'entries': entries})

from django.contrib.auth.views import LoginView
from django.shortcuts import render

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Point to your login template directly

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context
from django.shortcuts import get_object_or_404
from .models import Entry

def entry_detail(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    is_owner = entry.user == request.user  # Assuming you have a 'user' field in your Entry model
    return render(request, 'entry_detail.html', {'entry': entry, 'is_owner': is_owner})
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse

def custom_logout(request):
    logout(request)
    return redirect(reverse('index'))


from django.shortcuts import render, get_object_or_404
from .models import Profile
@login_required
def user_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)  # Creates a new profile if it doesn't exist
    return render(request, 'profile.html', {'profile': profile})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile  # Assuming you have a Profile model

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == 'POST':
        profile.bio = request.POST.get('bio')
        if request.FILES.get('profile_picture'):
            profile.profile_picture = request.FILES['profile_picture']
        profile.save()
        return redirect('user_profile')  # Redirect to the user profile page after saving

    return render(request, 'edit_profile.html', {'profile': profile})

import random

def my_entries(request):
    entries = Entry.objects.filter(user=request.user, deleted=False)

    # Define topic suggestions
    suggestion_topics = [
        "Reflect on a recent experience that changed your perspective.",
        "Write about a time when you overcame a challenge.",
        "Describe your goals for the next year.",
        "List three things you're grateful for and why.",
        "Write about a skill you want to improve and how you'll do it.",
        "Imagine your ideal day and describe it in detail.",
        "Write a letter to your future self.",
        "Describe a memorable journey you've taken and why it was special.",
        "Think about someone who inspires you and why.",
        "Write about a recent book or movie that impacted you.",
        "What does success mean to you?",
        "Reflect on a recent accomplishment you're proud of."
    ]

    # Pick 3 random suggestions
    suggestions = random.sample(suggestion_topics, 3)

    deleted_entries = Entry.objects.filter(user=request.user, deleted=True)

    # Pass entries, deleted_entries, and suggestions to the template
    return render(request, 'my_entries.html', {
        'entries': entries,
        'deleted_entries': deleted_entries,
        'suggestions': suggestions  # Ensure suggestions is here
    })

from django.urls import reverse
from django.http import HttpResponseRedirect

def permanently_delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id, user=request.user, deleted=True)
    entry.delete()  # Permanently deletes the entry from the database
    return HttpResponseRedirect(reverse('my_entries'))
