from django import template
from django.urls import reverse
from menu.models import MenuItem
from django.utils.safestring import mark_safe


register = template.Library()


def draw_menu_item(menu_item):
    html = ''
    html += '<li class="has-dropdown">'
    html += f'<a href="{reverse("xxx", args=[menu_item.url])}">{menu_item.name}</a>'
    return html


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu = MenuItem.objects.all()
    menu_item = menu.filter(url=menu_name).first()
    parents = menu_item.get_ancestors()
    children = list(menu.filter(parent__name=menu_name))

    html = ''
    for parent in parents:
        html += '<ul>'
        html += draw_menu_item(parent)

    html += '<ul>'
    html += draw_menu_item(menu_item)

    for child in children:
        html += '<ul>'
        html += draw_menu_item(child)
        html += '</ul>'

    html += '</ul>'

    return mark_safe(html)
