from django.contrib import admin
from django.urls import path, include
from menu.views import index, xxx

urlpatterns = [
    path('', index, name='index'),
    path('<str:menuitem_name>/', xxx, name='xxx'),
    path('admin/', admin.site.urls),
]
