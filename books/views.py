from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def quary_set_see(request):
	#данные
	#логика
	#рендеринг
	authors = Autor.objects.all()
	books = Book.objects.all()
	#author_new = Autor(name = 'Jonh',surname="Dou",date_birdthday='2022-04-05')
	#author_new.save()

	context= {
	'authors':authors,
	'books':books

	}




	return render(request,'books/base.html',context=context)

