﻿"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .forms import FeedbackForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.db import models
from .models import Comment 
from .forms import CommentForm 
from .models import Blog
from .forms import BlogForm


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница с нашими контактами.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Сведения о нас.',
            'year':datetime.now().year,
        }
    )

def links(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Полезные ресурсы',
            'year':datetime.now().year,
        }
    )



def pool(request):
    assert isinstance(request, HttpRequest)

    form = FeedbackForm()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return render(
                request,
                'app/pool.html',
                {
                    'form': form,
                    'thanks': True,
                }
            ) 
    else:
        form = FeedbackForm()
    
    return render(
        request,
        'app/pool.html',
        {
            'form': form,
            'thanks': False,
        }
    )


def registration(request):

    """Renders the registration page."""

    assert isinstance(request, HttpRequest)

    if request.method == "POST": # после отправки формы

        regform = UserCreationForm(request.POST)

        if regform.is_valid(): #валидация полей формы

            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы

            reg_f.is_staff = False # запрещен вход в административный раздел

            reg_f.is_active = True # активный пользователь

            reg_f.is_superuser = False # не является суперпользователем

            reg_f.date_joined = datetime.now() # дата регистрации

            reg_f.last_login = datetime.now() # дата последней авторизации

            reg_f.save() # сохраняем изменения после добавления данных
            login(request, reg_f)
            return redirect('home') # переадресация на главную страницу после регистрации

    else:

        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя

    return render(

        request,

        'app/registration.html',

        {
            'title': 'Регистрация',

            'regform': regform, # передача формы в шаблон веб-страницы

            'year':datetime.now().year,

        }

    )

def news(request):

    """Renders the blog page."""

    assert isinstance(request, HttpRequest)

    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели

    return render(

        request,

        'app/news.html',

        {

            'title':'Новости',

            'posts': posts, # передача списка статей в шаблон веб-страницы

            'year':datetime.now().year,

        }

    )

def newspost(request, parametr):

    """Renders the blogpost page."""

    assert isinstance(request, HttpRequest)

    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру

    comments = Comment.objects.filter(post=parametr)

    if request.method == "POST": # после отправки данных формы на сервер методом POST

        form = CommentForm(request.POST)

        if form.is_valid():

            comment_f = form.save(commit=False)

            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя

            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату

            comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий

            comment_f.save() # сохраняем изменения после добавления полей

            return redirect('newspost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария

    else:

        form = CommentForm() # создание формы для ввода комментария

    return render(

        request,

        'app/newspost.html',

        {
            'title': post_1.title,

            'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы

            'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы

            'form': form, # передача формы добавления комментария в шаблон веб-страницы

            'year':datetime.now().year,

        }

    )

def newpost(request):
    """Renders the new post page."""
    assert isinstance(request, HttpRequest)
    if request.method == "POST":

        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()
       
            return redirect('/newspost/{}'.format(blog_f.id))
    else:
            blogform = BlogForm()
    return render(
        request,
        'app/newpost.html',
        {
            'blogform': blogform,
            'title': 'Добавить статью блога',
            'year':datetime.now().year,
        }
    )

def videopost(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title': 'Видеоматериалы',
            'year': datetime.now().year,
        }
    )
