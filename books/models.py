from django.db import models

class Autor(models.Model):
	surname = models.CharField('Фамилия',max_length=100)#Фамилия
	name = models.CharField('Имя',max_length=100)#Имя 
	patronomic = models.CharField('Отчество',max_length=100,blank=True,null=True)# Отчество (не обязательно)
	date_birdthday = models.DateField('Дата рождения')# Дата рождения 
	class Meta:
		verbose_name = 'Автор'
		verbose_name_plural = 'Авторы'


	def __str__(self):
		return self.surname
	#возврат фамилия и имя
	#Класс мета

class Gangre(models.Model):
	name = models.CharField('Название',max_length=200)
	class Meta:
		verbose_name = 'Жанр'
		verbose_name_plural = 'Жанры'


	def __str__(self):
		return self.name
	#Название
	#возврат названия
	#класс мета

class Book(models.Model):
	nazva = models.CharField('Назва',max_length=200)
	mova = models.CharField('Мова',max_length=20)
	anotation = models.TextField('Анотація')
	image = models.ImageField('Изображение')
	file = models.FileField('Файл',blank=True,null=True)
	date_publication = models.DateField('Дата приема')
	gangre = models.ForeignKey(Gangre, related_name='Жанр', on_delete=models.CASCADE)
	author = models.ForeignKey(Autor, related_name='Автор', on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Книга'
		verbose_name_plural = 'Книги'


	def __str__(self):
		return self.nazva

