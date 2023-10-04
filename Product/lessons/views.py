import datetime

from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
import captcha

from .forms import *
from .models import *



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
    return ip


def save_user(request):
    '''функция сохранения действия пользователя на странице'''
    now = datetime.datetime.now()
    now_time = now.time()
    now_date = now.date()
    user = request.META['USERDOMAIN']
    ip = request.META['HTTP_HOST']
    date = now_date
    time = now_time
    # print(f'Здесь выводим наш request: {request.META}')  #Словарь, содержащий все доступные заголовки HTTP. Доступные заголовки зависят от клиента и сервера
    # for key,value in request.META.items():
    #    print(f"Ключ {key} : {value}")
    print(
        f"Компьютер пользователя - {request.META['USERDOMAIN']}, ip&port - {request.META['HTTP_HOST']}, дата: {now_date}, время: {now_time}")
    list = [user,ip,date,time]
    return list

def index(request):    # start page
    user = save_user(request)   #получаем данные о пользователях кто смотрит страницу
    try:
        question = AllUsers(
            username=user[0],
            ip_port=user[1],
            date=user[2],
            time=user[3]
            )
        question.save() # сохраняем полученный результат
    except Exception as e:
        print("Error saving question")


    products = Product.objects.all()
    category = Category.objects.all()
    lessons = Lesson.objects.all()
    context = {'products':products,
               'category':category,
               'lessons': lessons,
                'cat_selected': 0, #отображение всех записей}
               }

    return render(request, 'product/index.html',context=context)

def show_category(request,cat_id):
    '''Отображение на странице\ фильтрация отображаемых курсов'''
    products = Product.objects.filter(cat_id=cat_id)
    category = Category.objects.all()
    lessons = Lesson.objects.all()
    context = {'products': products,
               'category': category,
               'lessons': lessons,
               'cat_selected': cat_id,  # отображение нужной категории
               }

    #return HttpResponse(f'Отображение ктегории с id = {cat_id}')
    return render(request, 'product/index.html',context=context)

def show_lessons(request,lessons_id):   # настроить отображение урока на странице!!! потом разбираться с видео плеером!
    '''Функция отображения уроков по слагу'''
    post = get_object_or_404(Lesson, pk=lessons_id)
    context = {
        'post': post,
        'title': post.title_lesson,
        'cat_selected': 2,
    }
    return render(request,'product/post.html',context=context)
    #return HttpResponse(f"отображение урока с id = {lessons_id}")

def statistic(request):    # start page
    return render(request, 'product/statistica.html')

def contact(request):    # start page
    return render(request, 'product/contact.html')


def secsess_form(request):
    #redirect(request, 'monitoringi/monitoring.html')
    return render(request, 'product/secsess_form.html')  # redirect to start page on html



class LoginUser(LoginView):
    """Форма аутентификации на странице и личном кабинете"""
    form_class = LoginUserForm  #Используем свою форму для иутентификации а сайте
    #Django standart form to user authentification form_class = AuthenticationForm
    template_name = 'product/login.html'

    def get_success_url(self):
        return reverse_lazy('index')

def logout_user(request):
    """функция выхода пользователя со страницы"""
    logout(request)  # standart django method
    return render(request, 'product/index.html')


class RegisterUser(CreateView):
    """Регистрацияпользователя на данном ресурсе"""
    form_class = RegisterUserForm   #Django standart form to registration
    template_name = 'product/registration.html'    #ссылка на страницу
    success_url = reverse_lazy('index') #переадресация в случае удачной отправки

    def form_valid(self,form):
        """если пользователь ввел корректно все поля  то вызывается этот метод"""
        user = form.save()
        login(self.request,user)    #automatic avtorisation on sait
        return redirect('index')

