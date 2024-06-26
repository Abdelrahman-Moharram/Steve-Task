from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

import json
from .models import *
from .forms import BookForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        book_form = BookForm(json.loads(request.body))
        
        if book_form.is_valid():
            book_form = book_form.save()
            messages.success(request, message=f'Book {book_form.name} Added Successfully',extra_tags='success')
            return redirect(to='/')
        return HttpResponse(book_form.errors.as_json(), status = 400, content_type='application/json')
    return render(request, 'home/index.html', {'books': Book.objects.all()})


def update(request, id):
    if request.method == 'POST':
        book = Book.objects.get(id=id)
        book_form = BookForm(json.loads(request.body), instance=book)
        if book_form.is_valid():
            book_form = book_form.save()
            messages.success(request, message=f'Book {book_form.name} updated Successfully',extra_tags='success')
            return redirect(to='/')
        return HttpResponse(book_form.errors.as_json(), status = 400, content_type='application/json')
    

    book = list(Book.objects.filter(id=id).values()) 
    return JsonResponse(data={'book':book[0]})


def delete(request, id):
    Book.objects.filter(id=id).delete()
    messages.success(request, message=f'Book Delete Successfully',extra_tags='success')
    return redirect('/')


def details(request, id):
    return render(request, 'home/index.html', {})
