from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.index, name = 'list'),
    path('info/', views.info, name = 'information'),
    path('schedule/', views.schedules, name='schedule'),
    path('schedule/target1/', views.target1, name = 'target1' ),
    path('schedule/target2/', views.target2, name = 'target2' ),
    path('schedule/target3/', views.target3, name = 'target3' ),
    path('schedule/target4/', views.target4, name = 'target4' ),
    path('schedule/target5/', views.target5, name = 'target5' ),
    path('schedule/target6/', views.target6, name = 'target6' ),
    path('schedule/target7/', views.target6, name = 'target7' ),
    path('schedule/target8/', views.target6, name = 'target8' ),
    path('link/<int:lodge_id>', views.targetLink, name='link')
]