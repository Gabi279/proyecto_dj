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
        
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre de usuario ...',
                    'class': 'input-group-field',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electronico ...',
                    'class': 'input-group-field',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre ...',
                    'class': 'input-group-field',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Apellido ...',
                    'class': 'input-group-field',
                }
            ),
            'phone': forms.NumberInput(
                attrs={
                    'placeholder': 'Teléfono ...',
                    'class': 'input-group-field',
                }
            ),
            'rol': forms.Select(
                attrs={
                    'placeholder': 'Rol ...',
                    'class': 'input-group-field',
                }
            ),
            'is_active': forms.CheckboxInput(
                attrs={
                    'placeholder': 'Rol ...',
                    'class': 'input-group-field',
                },
            ),
        }
    
        password1 = forms.CharField(
            label='Contraseña',
            required=True,
            widget=forms.PasswordInput(
                attrs={'placeHolder': 'Contraseña actual'}
            )
        )
        
        password2 = forms.CharField(
            label='Contraseña',
            required=True,
            widget=forms.PasswordInput(
                attrs={'placeHolder': 'Contraseña nueva'}
            )
        )
