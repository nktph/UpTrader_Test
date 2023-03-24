from django.shortcuts import render
from menu.models import MenuItem


def index(request):
    menu_name = 'main_menu'
    context = {'menu_name': menu_name}
    return render(request, 'index.html', context)


def xxx(request, menuitem_name):
    menu_name = menuitem_name
    context = {'menu_name': menu_name}
    return render(request, 'index.html', context)
