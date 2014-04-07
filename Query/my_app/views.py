from django.shortcuts import render
from .models import Libro
# Create your views here.


def my_exact(request):
	libros = Libro.objects.filter(editor__exact= 'aaa')
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query EXACT'}
	return render(request,'query.html',dic) 

def my_iexact(request):
	libros = Libro.objects.filter(editor__iexact= 'aaa')
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  IEXACT'}
	return render(request,'query.html',dic) 

def my_contains(request):
	libros = Libro.objects.filter(autor__contains= 'Parlatu')
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  CONTAINS'}
	return render(request,'query.html',dic)

def my_icontains(request):
	libros = Libro.objects.filter(autor__icontains= 'parlatu')
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  ICONTAINS'}
	return render(request,'query.html',dic)

def my_in(request):
	libros = Libro.objects.filter(id__in= [3,9,34,222])
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  IN'}
	return render(request,'query.html',dic)


def my_gt(request):
	libros = Libro.objects.filter(fecha_publicacion__gt = '2010-08-12' )
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  GT'}
	return render(request,'query.html',dic)

def my_gte(request):
	libros = Libro.objects.filter(fecha_publicacion__gte= '2010-08-12' )
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  GTE'}
	return render(request,'query.html',dic)

def my_lt(request):
	libros = Libro.objects.filter(fecha_publicacion__lt= '2010-08-12')
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  LT'}
	return render(request,'query.html',dic)

def my_lte(request):
	libros = Libro.objects.filter(fecha_publicacion__lte= '2010-08-12')
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  LTE'}
	return render(request,'query.html',dic)


def my_startswith(request):
	libros = Libro.objects.filter(editor__startswith= 'Odio')
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  STARTSWITH'}
	return render(request,'query.html',dic)

def my_istartswith(request):
	libros = Libro.objects.filter(editor__istartswith= 'odio')
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  ISTARTSWITH'}
	return render(request,'query.html',dic)

def my_endswith(request):
	libros = Libro.objects.filter(editor__endswith= 'Mo')
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  ENDSWITH'}
	return render(request,'query.html',dic)

def my_iendswith(request):
	libros = Libro.objects.filter(editor__iendswith= 'mo')
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  IENDSWITH'}
	return render(request,'query.html',dic)

def my_range(request):
	#libros = Libro.objects.filter(id__range= (9990,9999))
	libros = Libro.objects.filter(fecha_publicacion__range= ('2010-09-26','2010-10-03'))
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  IENDSWITH'}
	return render(request,'query.html',dic)

def my_year(request):
	libros = Libro.objects.filter(fecha_publicacion__year = 2014)
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  IENDSWITH'}
	return render(request,'query.html',dic)

def my_month(request):
	libros = Libro.objects.filter(fecha_publicacion__month = 12)
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  IENDSWITH'}
	return render(request,'query.html',dic)

def my_day(request):
	libros = Libro.objects.filter(fecha_publicacion__day = 13)
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  IENDSWITH'}
	return render(request,'query.html',dic)


def my_isnull(request):
	libros = Libro.objects.filter(editor__isnull = True)
	dic = {'libros': libros , 'titulo':'Ejemplo sobre el query  IENDSWITH'}
	return render(request,'query.html',dic)

