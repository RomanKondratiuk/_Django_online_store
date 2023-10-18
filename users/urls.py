from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users import views
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, EmailVerify, MyPasswordResetView, TemporaryPasswordLoginView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    # path('confirm_email/<str:token>/', views.ConfirmEmailView.as_view(), name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('password_reset/', MyPasswordResetView.as_view(), name='password_reset'),
    path('login_with_temp_password/', TemporaryPasswordLoginView.as_view(), name='login_with_temp_password'),

]