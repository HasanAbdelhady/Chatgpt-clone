from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from .forms import CustomUserCreationForm, CustomUserChangeForm, PasswordChangeForm
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.urls import reverse_lazy
from django.db import transaction

User = get_user_model()

class UserRegistrationView(View):
    @method_decorator(csrf_protect)
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('chat')
        form = CustomUserCreationForm()
        return render(request, 'users/register.html', {'form': form})

    @method_decorator(csrf_protect)
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('chat')
        
        form = CustomUserCreationForm(request.POST, request.FILES)
        print(request.POST)
        
        if form.is_valid():
            with transaction.atomic():
                user = form.save(commit=False)
                
                user.save()

                login(request, user)
                
                messages.success(
                    request, 'Your account has been created! You can now start chatting.')
                return redirect('new_chat')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
        
        return render(request, 'users/register.html', {'form': form})

class UserLoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_form = CustomUserChangeForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user)
        context = {
            'user_form': user_form,
            'password_form': password_form,
        }
        return render(request, 'users/profile.html', context)
    def handle_password_change(self, request):
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Password updated successfully!')
        else:
            for field, errors in password_form.errors.items():
                for error in errors:
                    messages.error(request, f'Password {field}: {error}')
        return redirect('profile')
    def post(self, request):
        action = request.POST.get('action')
        print(request.POST)
        if action == 'update_profile':
            user_form = CustomUserChangeForm(
                request.POST, request.FILES, instance=request.user
            )
            if user_form.is_valid():
                user = user_form.save(commit=False)

                user.save()

                messages.success(request, 'Profile updated successfully!')
            else:
                for field, errors in user_form.errors.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')

        elif action == "change_password":
            return self.handle_password_change(request)

        return redirect('profile')

class TokenObtainPairView(APIView):
    def post(self, request):
        user = request.user
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class TokenRefreshView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh = request.data.get('refresh')
            token = RefreshToken(refresh)
            return Response({
                'access': str(token.access_token),
                'refresh': str(token),
            })
        except Exception as e:
            return Response({'error': 'Invalid refresh token'}, status=400)


class TokenObtainPairView(APIView):
    def post(self, request):
        user = request.user
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class TokenRefreshView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh = request.data.get('refresh')
            token = RefreshToken(refresh)
            return Response({
                'access': str(token.access_token),
                'refresh': str(token),
            })
        except Exception as e:
            return Response({'error': 'Invalid refresh token'}, status=400)


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect(self.next_page)
