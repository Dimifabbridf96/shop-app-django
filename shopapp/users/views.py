from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserUpdateForm, MessageFilterForm, LoginForm
from .models import CustomUser, Message
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please enter a username and password.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            image = form.cleaned_data['image']
            CustomUser.objects.create_user(username=username, email=email, password=password, image=image )
            messages.success(request, 'Registration successful')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request,('Logout successful'))
    return redirect('home')
@login_required
def profile(request):
    user = request.user
    all_users = CustomUser.objects.exclude(pk=user.pk)
    
    filter_form = MessageFilterForm(request.GET)

    if filter_form.is_valid():
        messages = filter_form.filter_messages(Message.objects.all())

    if request.method == 'GET':
        sender_pk = request.GET.get('sender')
        if sender_pk:
            messages = Message.objects.filter(recipient=user, sender_id=sender_pk)
        else:
            messages = Message.objects.filter(recipient=user)
    else:
        recipient_pk = request.POST.get('recipient')
        subject = request.POST.get('subject')
        content = request.POST.get('content')

        recipient = User.objects.get(pk=recipient_pk)
        message = Message(sender=user, recipient=recipient, subject=subject, content=content)
        message.save()

        messages = Message.objects.filter(recipient=user)

    return render(request, 'registration/accounts.html', {
        'user': user,
        'all_users': all_users,
        'messages': messages,
    })

def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.username = request.user.username
            messages.warning(request, 'Your Details Have Been Updated')
            messages.warning(request, 'Thank you for updating your personal and contact details.')
            
            form.instance.save()
            return render(request, 'registration/accounts.html')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'registration/accounts.html', {'form': form})

def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            domain = request.get_host()
            protocol = 'https' if request.is_secure() else 'http'
            email_subject = 'Password Reset Request'
            email_body = render_to_string('password_reset_email.html', {
                'user': user,
                'domain': domain,
                'protocol': protocol,
                'uidb64': uidb64,
                'token': token,
            })
            send_mail(email_subject, email_body, 'your_email_address@example.com', [email])
            return redirect('password_reset_done')
    return render(request, 'password_reset_form.html')

def password_reset_done(request):
    return render(request, 'password_reset_done.html')

def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and PasswordResetTokenGenerator().check_token(user, token):
        # Allow the user to reset their password
        # ...
        return render(request, 'password_reset_confirm.html')
    else:
        return redirect('password_reset_done')

def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')


def delete_account(request, account_id):
    user = request.user

    if user.is_superuser:
        # Admin account deletion
        account = CustomUser.objects.get(pk=account_id)
        account.delete()
        messages.success(request, f'Account {account.username} deleted successfully')
        return redirect('profile')
    else:
        # Personal account deletion
        user.delete()
        logout(request)
        messages.success(request, 'Your account has been deleted')
        return redirect('login')
