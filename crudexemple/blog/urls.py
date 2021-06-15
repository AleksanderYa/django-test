from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('lol/', views.post_list_two, name='post-list-two'),
]
