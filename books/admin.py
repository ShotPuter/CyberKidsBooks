from django.contrib import admin

from .models import Book,Autor,Gangre
# Register your models here.

class AdminAutor(admin.ModelAdmin):
	list_display = ['surname','name','patronomic']
	empty_value_display = '-empty-'


admin.site.register(Book)
admin.site.register(Autor,AdminAutor)
admin.site.register(Gangre)