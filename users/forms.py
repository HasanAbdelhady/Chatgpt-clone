from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-100'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-100'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-100'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-100'
        })
    )
    
    profile_image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'hidden',
            'accept': 'image/*'
        })
    )

    class Meta:
        model = CustomUser
        fields = (
            'username', 'email', 'profile_image'
        )

    def clean_username(self):
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username


class CustomUserChangeForm(UserChangeForm):
    password = None  # Remove password field from the form

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-100'
        })
    )
    profile_image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'hidden',
            'accept': 'image/*'
        })
    )


    class Meta:
        model = CustomUser
        fields = (
            'email', 'profile_image'
        )

class PasswordChangeForm(SetPasswordForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-100'
        })
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-100'
        })
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-100'
        })
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(user, *args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('Your old password was entered incorrectly.')
        return old_password
