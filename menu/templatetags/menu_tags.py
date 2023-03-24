from django import template
from django.urls import reverse
from menu.models import MenuItem
from django.utils.safestring import mark_safe


register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu = MenuItem.objects.all()
    menu_item = menu.filter(url=menu_name)
    parents = menu_item[0].get_ancestors()
    children = list(menu.filter(parent__name=menu_name))

    html = ''
    for parent in parents:
        html += '<ul>'
        html += '<li class="has-dropdown">'
        html += f'<a href="{reverse("xxx", args=[parent.url])}">{parent.name}</a>'

    html += '<ul>'
    html += '<li class="has-dropdown">'
    html += f'<a href="{reverse("xxx", args=[menu_item[0].url])}"><i>{menu_item[0].name}</i></a>'

    for child in children:
        html += '<ul>'
        html += '<li class="">'
        html += f'<a href="{reverse("xxx", args=[child.url])}">{child.name}</a>'
        html += '</ul>'

    html += '</ul>'

    return mark_safe(html)
