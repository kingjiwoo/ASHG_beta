from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import static
from django.conf import settings

urlpatterns = [
    path('lodge/', include('lodge.urls')),
    path('manager/', include('manager.urls')),
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

]