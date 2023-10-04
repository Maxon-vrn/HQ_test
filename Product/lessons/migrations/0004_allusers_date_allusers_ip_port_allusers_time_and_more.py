# Generated by Django 4.2.3 on 2023-10-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_lesson_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='allusers',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='дата'),
        ),
        migrations.AddField(
            model_name='allusers',
            name='ip_port',
            field=models.CharField(max_length=30, null=True, verbose_name='Ip and Port'),
        ),
        migrations.AddField(
            model_name='allusers',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True, verbose_name='время'),
        ),
        migrations.AlterField(
            model_name='allusers',
            name='username',
            field=models.CharField(max_length=100, null=True, verbose_name='Компьютер пользователя'),
        ),
    ]
