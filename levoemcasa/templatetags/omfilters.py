from django import template

register = template.Library()


@register.filter
def format_price(val):
    return f'R$ {val:.2f}'.replace('.', ',')
