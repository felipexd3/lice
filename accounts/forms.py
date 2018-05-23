from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User as UserAdmin

User = get_user_model()

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha')
    password2 = forms.CharField(label='Confirmar Senha')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Senhas não conferem')
            return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = UserAdmin
        fields = ['first_name', 'last_name', 'email', 'active', 'is_staff', 'is_admin']

class UserAdminForm(forms.ModelForm):
    class Meta:
        model = UserAdmin
        fields = ['first_name', 'last_name', 'email']
