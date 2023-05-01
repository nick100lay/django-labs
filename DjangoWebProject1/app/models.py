﻿"""
Definition of models.
"""

from email.policy import default
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User


class Blog(models.Model):
    
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголоnок")

    description = models.TextField(verbose_name = "Краткoе содержание")
    
    content = models.TextField(verbose_name = "Полное содернание")
    
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")

    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")

    image = models.FileField(default = 'temp.jpg', verbose_name = 'Путь к картинке')

    def get_absolute_url(self): # метод возврацает строку с URL-адpесом записи

        return reverse("blogpost", args=[str(self.id)])

    def  __str__(self): # метод возвращает название, используемое для представления отдельных записей в административном разделе

        return self.title
    
    class Meta:
        
        db_table = "Posts" # иия таблицы для модели
        
        ordering = ["-posted"] # порядок сортировки данных в модели (*-* означает по убыванию)
        
        verbose_name = "статья блога" # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
        
        verbose_name_plural = "статьи блогa" # тоже для всех статей блога
        
admin.site.register(Blog)


class Comment(models.Model):

    text = models.TextField(verbose_name = "Текст комментария")
    
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата комментария")
    
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор комментария")

    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья комментария")
    
    def __str__(self): # метод позпращает название, используеное для представления отдельных записей в административном разделе
        return 'Комментрарий %d %s к %s' % (self.id, self.author, self.post)

    class Meta:
        db_table = "Comment"
        
        ordering = ["-date"]
        
        verbose_name = "Комментарии и статье блога"
        
        verbose_name_plural = "Комментарии и статьям блога"
        

admin.site.register(Comment)

    
