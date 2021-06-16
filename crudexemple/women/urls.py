from django.contrib import admin
from django.urls import path, re_path, include
from .views import *
  

urlpatterns = [
    
    path('', index,name='home'),
    path('cats/', categories),
    path('lol/', include('blog.urls')),
    
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
 
]


#handler404 = pageNotFound