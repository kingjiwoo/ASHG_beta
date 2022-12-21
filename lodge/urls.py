from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'lodge'

urlpatterns = [
    path('', views.index, name = 'list'),
    path('info/', views.info, name = 'information'),
    path('report/', views.report, name='report'),
    path('report/clean/', views.clean, name='clean'),
    path('report/details/', views.details, name='details'),

]