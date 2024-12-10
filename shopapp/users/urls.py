from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('user/update/', views.update_profile, name='update_profile'),
    path('register/', views.register, name='register'),
    path('accounts/logout/', views.logout_view , name='logout'),
    path('delete_accounts/<int:account_id>', views.delete_account, name='delete_account'),
    path('password_reset/', PasswordResetView.as_view(template_name='password_reset_form.html', email_template_name='password_reset_email.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]   