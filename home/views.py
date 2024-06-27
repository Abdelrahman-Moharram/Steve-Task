from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.http import HttpResponseNotFound

import json
from .models import *
from .forms import BookForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST, request.FILES)
        
        if book_form.is_valid():
            book_form = book_form.save()
            messages.success(request, message=f'Book {book_form.name} Added Successfully',extra_tags='success')
            return redirect("/")
        return JsonResponse(data={'errors':book_form.errors.as_json()}, status=400, content_type='application/json')
    
    return render(request, 'home/index.html', {
        'books': Book.objects.all(), 
        'categories': Category.objects.all(), 
        'authors': Author.objects.all()
        })


def details(request, id):
    try:
        return render(request, 'home/details.html', 
            {
                'book':Book.objects.get(id=id), 
                'books':Book.objects.exclude(id=id).order_by('price').all()[0:4]
            }
        )
    except:
        return HttpResponseNotFound('<h1 style="text-align:center;margin-top:40px">This Book is Not Found</h1>')


def update(request, id):
    if request.method == 'POST':
        book = Book.objects.get(id=id)
        book_form = BookForm(request.POST, request.FILES, instance=book)
        if book_form.is_valid():
            book_form = book_form.save()
            messages.success(request, message=f'Book {book_form.name} updated Successfully',extra_tags='success')
            return HttpResponse({}, status = 200, content_type='application/json')
        return HttpResponse(book_form.errors.as_json(), status = 400, content_type='application/json')
    

    book = list(Book.objects.filter(id=id).values()) 
    return JsonResponse(data={'book':book[0]})


def delete(request, id):
    Book.objects.filter(id=id).delete()
    messages.success(request, message=f'Book Delete Successfully',extra_tags='success')
    return redirect('/')



def multiplication(request):
    number = request.GET.get('number')
    if not number:
        return HttpResponseNotFound('<h1 style="text-align:center;margin-top:40px">Number Shouldn\'t be Null or Empty</h1>')
    if not number.isnumeric():
        return HttpResponseNotFound(f'<h1 style="text-align:center;margin-top:40px">"{number}" Number is Not a Valid Number</h1>')

    return render(request, 'home/multiplication.html', {'number': int(number)})