from django.contrib import admin
from django.urls import path 
from .import views

urlpatterns = [
   path('',views.landing,name='landing'),
   
   #path('dashboard',views.dashboard,name='dashboard'),
   #path('archieve',views.archieve,name='archieve'),
   path('page1',views.page1,name='page1'),
   path('page2',views.page2,name='page2'),
   
  
   
]