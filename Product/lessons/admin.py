from django.contrib import admin

# Register your models here.
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display =('owner','lesson','subject','is_published','time_create','time_update')
    list_display_list = ('owner','lesson','subject','is_published','time_create','time_update')
    search_fields = ('owner','lesson','subject','is_published','time_create','time_update')

class LessonAdmin(admin.ModelAdmin):
    list_display =('title_lesson','video','views','is_published')
    list_display_list = ('title_lesson', 'video', 'views', 'is_published')
    search_fields = ('title_lesson', 'video', 'views', 'is_published')


class AllUsersAdmin(admin.ModelAdmin):
    list_display = ('ip_port', 'username','date', 'time', 'time_watch','video','is_viewed')
    llist_display_list = ('ip_port', 'username','date', 'time', 'time_watch','video','is_viewed')
    search_fields = ('ip_port', 'username','date', 'time', 'time_watch','video','is_viewed')



admin.site.register(Lesson,LessonAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Owner)
admin.site.register(AllUsers,AllUsersAdmin)
admin.site.register(Category)
