#You'll only need this in case you wanted to use a front-end framework (to get proper api endpoints)
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'profile_image']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 before creating user
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        if 'profile_image' in validated_data:
            user.profile_image = validated_data['profile_image']
            
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'profile_image', 'username']
        read_only_fields = ['username']  # Username cannot be changed

    def update(self, instance, validated_data):
        # Handle email update
        if 'email' in validated_data:
            new_email = validated_data['email']
            if User.objects.exclude(pk=instance.pk).filter(email=new_email).exists():
                raise serializers.ValidationError({"email": "This email is already in use."})
            instance.email = new_email

        # Handle profile image update
        if 'profile_image' in validated_data:
            instance.profile_image = validated_data['profile_image']

        instance.save()
        return instance

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs