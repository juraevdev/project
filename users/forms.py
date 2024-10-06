from django import forms
from .models import CustomUser

class RegisterUserForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    def create(self, validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        user = CustomUser.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
            email = email,
        )
        return user
    
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)