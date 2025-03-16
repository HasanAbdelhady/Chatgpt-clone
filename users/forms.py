from .models import CustomUser, Interest
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


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

    learning_style_visual = forms.IntegerField(initial=0, required=False)
    learning_style_auditory = forms.IntegerField(initial=0, required=False)
    learning_style_kinesthetic = forms.IntegerField(initial=0, required=False)
    learning_style_reading = forms.IntegerField(initial=0, required=False)

    interests = forms.ModelMultipleChoiceField(
        queryset=Interest.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple()
    )
    custom_interests = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'w-full p-2 border border-gray-300 rounded-lg',
            'placeholder': 'Enter additional interests...'
        })
    )

    study_habits = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'w-full p-2 border border-gray-300 rounded-lg',
            'placeholder': 'Describe your study habits...'
        })
    )
    preferred_study_time = forms.ChoiceField(
        choices=CustomUser.STUDY_TIME_CHOICES,
        widget=forms.Select(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'})
    )
    quiz_preference = forms.ChoiceField(
        choices=CustomUser.QUIZ_PREFERENCE_CHOICES,
        widget=forms.Select(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'})
    )

    class Meta:
        model = CustomUser
        fields = (
            'email', 'profile_image', 'learning_style_visual', 'learning_style_auditory',
            'learning_style_kinesthetic', 'learning_style_reading', 'interests',
            'custom_interests', 'study_habits', 'preferred_study_time', 'quiz_preference'
        )


class PasswordChangeForm(forms.Form):
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

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError(
                "The two password fields didn't match.")
        return cleaned_data
