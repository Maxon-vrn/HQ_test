from django.db import models
from django.urls import reverse


# Create your models here.
class Owner(models.Model):
    '''Владелец курсов'''
    owners = models.CharField(max_length=100, db_index=True,verbose_name='Автор')

    def __str__(self):
        return self.owners

    class Meta:
        verbose_name = "Автор"  # форимируем название в админ панели на русскаом
        verbose_name_plural = 'Автор'

class Lesson(models.Model):
    '''Урок'''
    title_lesson = models.CharField(max_length=100,verbose_name='Название урока')
    video = models.URLField(max_length=200,verbose_name='Ссылка на видео')   # video link
    time_video = models.CharField(max_length=20)    # время длительности видео в секундах!
    views = models.IntegerField(default=0,verbose_name='количество просмотров')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    slug = models.SlugField(max_length=255,unique=True, db_index=True, verbose_name='URL',null=True)

    def __str__(self):
        return self.title_lesson

    class Meta:
        verbose_name = "Уроки"  # форимируем название в админ панели на русскаом
        verbose_name_plural = 'Уроки'


class Product(models.Model):
    '''Таблица продукта сводная'''
    owner = models.ForeignKey(Owner,on_delete=models.PROTECT,verbose_name='Владелец')
    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT,verbose_name='Урок')    #по id урока будет доступ
    subject = models.CharField(max_length=100,verbose_name='Тема')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления',null=True)
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL',null=True)

    def __str__(self):
        return self.owner

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    class Meta:
        verbose_name = "Курсы"  # форимируем название в админ панели на русскаом
        verbose_name_plural = 'Курсы'
        ordering = ['time_create']  # сортировка по каким полям производится


class AllUsers(models.Model):
    '''Все пользователи кто просматривает\просматривал видео'''
    username = models.CharField(max_length=100,verbose_name='Компьютер пользователя',null=True)
    ip_port = models.CharField(max_length=30,verbose_name='Ip and Port',null=True)
    date = models.DateField(auto_now_add=True,verbose_name='дата', null=True)
    time = models.TimeField(auto_now_add=True,verbose_name='время',null=True)
    time_watch = models.DateTimeField(auto_now_add=True,verbose_name='время просмотра',null=True)    #время когда просматривал видео
    video = models.ForeignKey(Lesson,on_delete=models.PROTECT,verbose_name='видео урока',null=True)
    is_viewed = models.BooleanField(default=True, verbose_name='Просмотрено',null=True)   #Просмотрено видео на 80% или нет


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователи ресурса"  # форимируем название в админ панели на русскаом
        verbose_name_plural = 'Пользователи ресурса'

class Category(models.Model):
    '''К какой категории относится продукт'''
    category = models.CharField(max_length=20,db_index=True,verbose_name='Категория')

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Категория"  # форимируем название в админ панели на русскаом
        verbose_name_plural = 'Категория'