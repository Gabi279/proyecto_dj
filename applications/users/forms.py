from django import forms
from django.contrib.auth import authenticate

from .models import User

class UserRegisterForm(forms.ModelForm):
    
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeHolder': 'Contraseña'}
        )
    )
    password2 = forms.CharField(
    label='Contraseña',
    required=True,
    widget=forms.PasswordInput(
        attrs={'placeHolder': 'Repetir contraseña'}
    )
)
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'name',
            'last_name',
            'phone',
            'rol',
            'is_active',
        )

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no coinciden')
            
class LoginForm(forms.Form):
        username = forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={'placeHolder': 'username'}
        )
    )

        password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeHolder': 'Contraseña'}
        )
    )
        
        def clean(self):
            cleaned_data = super(LoginForm, self).clean()
            username = self.cleaned_data["username"]
            password = self.cleaned_data["password"]
            
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Revise usuario o contraseña')
            return self.cleaned_data
    
class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )