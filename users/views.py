from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import View
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# class ConfirmEmailView(View):
#     def get(self, request, token):
#         User = get_user_model()
#         try:
#             user = User.objects.get(email_verification_token=token)
#             user.is_active = True
#             user.email_verification_token = None  # delete token
#             user.save()
#             messages.success(request, 'Your email has been successfully confirmed. You can now log in.')
#         except User.DoesNotExist:
#             messages.error(request, 'Invalid email verification token.')
#         return redirect('users:login')


# class RegisterView(CreateView):
#     model = User
#     form_class = UserRegisterForm
#     template_name = 'users/register.html'
#     success_url = reverse_lazy('users:login')
#
#     def form_valid(self, form):
#         # We create a user, but do not save it yet
#         user = form.save(commit=False)
#
#         # Additional logic for sending a confirmation email
#         user.generate_email_verification_token()  # Generating a token
#         user.is_active = False  # Making the user inactive until the email is confirmed
#         user.save()
#
#         # send an email with a link to confirm your email
#         self.send_verification_email(user)
#
#         # return super().form_valid(form)
#         return render(self.request, 'users/verification_sent.html')
#
#     def send_verification_email(self, user):
#         # Generating a URL with a token to confirm your email
#         verification_url = self.request.build_absolute_uri(
#             reverse('users:confirm_email', args=[user.email_verification_token]))
#
#         # send an email with a link to confirm your email
#         subject = 'Confirmation email'
#         message = f'To confirm your email, follow the following link:\n\n{verification_url}'
#         from_email = settings.EMAIL_HOST_USER  # local email
#         recipient_list = [user.email]
#         send_mail(subject, message, from_email, recipient_list)


def send_verify_email_message(verification_url, recipient_email):
    # SMTP server settings
    smtp_host = 'smtp.mail.ru'
    smtp_port = 2525
    smtp_user = settings.EMAIL_HOST_USER
    smtp_password = 'ad8GfSyfvhZuqzu5fAX3'

    # Creating a letter
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = recipient_email
    msg['Subject'] = 'Confirmation email'

    # Text of the letter
    email_content = f'To confirm your email, follow the following link: {verification_url}'
    msg.attach(MIMEText(email_content, 'plain'))

    # Establishing a connection to an SMTP server
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()  # use TLS
    server.login(smtp_user, smtp_password)

    # Sending letter
    server.sendmail(smtp_user, recipient_email, msg.as_string())

    # Closing a connection
    server.quit()


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form: UserRegisterForm):
        user: User = form.save()
        send_verify_email_message(verification_url=self.get_verify_email_url(user), recipient_email=user.email)
        messages.info(self.request, 'Подтвердите почту, чтобы завершить регистрацию')
        # return redirect('users:login')
        return render(self.request, 'users/verification_sent.html')

    def get_verify_email_url(self, user) -> str:
        current_site = get_current_site(self.request)
        domain = current_site.domain
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        url_path = reverse('users:verify_email', kwargs={'uidb64': uid, 'token': token})
        return f'http://{domain}{url_path}'


class EmailVerify(View):
    def get(self, request: HttpRequest, uidb64: str, token: str):
        user = self.get_user(uidb64)
        if not user or not default_token_generator.check_token(user, token):
            messages.warning(self.request, 'Invalid reset link, please try to get it again')
        else:
            messages.success(self.request, 'Email successfully confirmed')
            user.is_active = True
            user.save()
        return redirect('users:login')

    def get_user(self, uid_base64: str) -> User | None:
        try:
            uid = urlsafe_base64_decode(uid_base64).decode()
            user_id = int(uid)
            user = User.objects.get(pk=user_id)
        except (ValueError, User.DoesNotExist):
            user = None
        return user


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
