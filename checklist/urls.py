from django.urls import path
from . import views

app_name = 'checklist'

urlpatterns = [
    path('<int:lodge_id>/<str:room_num>/', views.index, name = 'checklist'),
    path('post/<int:lodge_id>/<str:room_num>/', views.checkListPost, name = 'post'),
]