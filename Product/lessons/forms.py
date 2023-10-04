from multiprocessing import AuthenticationError
from xml.dom import ValidationErr
from django import forms

from .models import *
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget,AdminSplitDateTime
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
import re
from captcha import *    #don`t see this module
from captcha.fields import CaptchaField


#AddPostForm
class RegisterUserForm(UserCreationForm):
    """Форма для регистрации новых посетителей на сайте(требующих авторизации)"""
    username = forms.CharField(label='Имя', widget=forms.TextInput())
    login = forms.CharField(label='Логин', widget=forms.TextInput())
    phone = forms.CharField(label='Телефон',widget=forms.TextInput)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())
    captcha = CaptchaField()

    class Meta():
        model = User    # это название бд где хранятся данные
        fields = ['username','login', 'phone', 'password1', 'password2']  # nomber phone,'first_name' - need to past
        widgets = {
        }

class LoginUserForm(AuthenticationForm):
    """Вход пользователя на сайт """
    username = forms.CharField(label='Логин',widget=forms.TextInput())
     #widget=forms.TextInput(attrs{'class': 'form-input'}) оформление поля через стили css
    password = forms.CharField(label="Пароль", widget=forms.TextInput())

