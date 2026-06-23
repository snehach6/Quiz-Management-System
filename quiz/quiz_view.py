from django.urls import path
from . import quiz_view   # import from quiz_view.py

urlpatterns = [
    path('', quiz_view.quiz_view, name='quiz'),
    path('result/', quiz_view.result_view, name='result'),
]
