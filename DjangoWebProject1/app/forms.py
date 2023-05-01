"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Пароль"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Пароль'}))


class FeedbackForm(forms.Form):
    who = forms.ChoiceField(label='Кто вы?',
                                choices=(
                                    ('Работник', 'Работник'),
                                    ('Безработный', 'Безработный'),
                                    ('Студент', 'Студент'),
                                    ('Школьник', 'Школьник')),
                                widget=forms.Select({
                                    'class': 'form-control'
                                }) 
                                )

    city = forms.CharField(label='Ваш город', min_length=2, max_length=100,
                            widget=forms.TextInput({
                                'class': 'form-control'
                            }))
    occupation = forms.CharField(label='Ваш род занятий', min_length=2, max_length=100,
                                    widget=forms.TextInput({
                                        'class': 'form-control'
                                    }))

    gender = forms.ChoiceField(label='Ваш пол',
                               choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')],
                               widget=forms.RadioSelect)

    rating = forms.ChoiceField(label='Ваща оценка сайта',
                                 choices=(
                                    ('Великолепно', 'Великолепно'),
                                    ('Хорошо', 'Хорошо'),
                                    ('Посредственно', 'Посредственно'),
                                    ('Плохо', 'Плохо')), 
                                initial=1,
                                widget=forms.Select({
                                    'class': 'form-control'
                                }))

    notice = forms.BooleanField(label='Хотите ли получать новости сайта на e-mail?',
                                required=False, widget=forms.CheckboxInput({
                                    'class': 'form-check-input'
                                }))

    email = forms.EmailField(label='Ваш e-mail', min_length=7,
                                widget=forms.TextInput({
                                    'class': 'form-control'
                                }))
    wish = forms.CharField(label='Ваши пожелания по поводу сайта',
                              widget=forms.Textarea(
                                attrs={'class': 'form-control', 'rows': 12, 'cols': 20}
                                ))

class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment # используемая модель

        fields = ('text',) # требуется заполнить только поле text

        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title' : "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image' : "Картинка"}

