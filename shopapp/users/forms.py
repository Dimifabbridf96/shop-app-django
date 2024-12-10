from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from .models import CustomUser

class LoginForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if not username or not password:
            raise ValidationError('Please enter a username and password.')

        user = CustomUser.objects.filter(username=username).first()

        if user is not None and not user.check_password(password):
            raise ValidationError('Invalid username or password.')

        return self.cleaned_data


class CustomUserCreationForm(forms.Form):
    image = forms.ImageField()
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError('This username is already taken.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('This email address is already registered.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError('The passwords do not match.')
        return password2
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']
        
class MessageFilterForm(forms.Form):
    sender = forms.ModelChoiceField(queryset=CustomUser.objects.all(), required=False)
    
    def filter_messages(self, queryset):
        sender = self.cleaned_data['sender']
        if sender:
            queryset = queryset.filter(sender=sender)
        return queryset