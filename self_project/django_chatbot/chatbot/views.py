from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Make sure you replace 'input-your-key' with your actual OpenAI API key
openai_api_key = 'input-your-key'
openai.api_key = openai_api_key

def ask_openai(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ]
        )
        # Log the full response from OpenAI
        print(f"OpenAI response: {response}")
        
        # Extract and return the answer
        answer = response['choices'][0]['message']['content'].strip()
        return answer
    
    except Exception as e:
        # Log any errors that occur
        print(f"Error calling OpenAI API: {e}")
        return "Sorry, I'm having trouble responding right now. Please try again later."

@login_required
def chatbot(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        print(f"Received message from user: {message}")
        
        response = ask_openai(message)
        print(f"Response from OpenAI: {response}")

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        
        return JsonResponse({'message': message, 'response': response})
    
    return render(request, 'chatbot.html', {'chats': chats})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('main')
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Passwords do not match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
def home(request):
    return render(request,'home.html')

def main(request):
    return render(request,'main.html')

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            send_mail(
                f"New contact: {contact.name}",
                contact.message,
                contact.email,
                ['sahanaanjus@gmail.com'],
            )
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
def success_view(request):
    return render(request, 'success.html')
