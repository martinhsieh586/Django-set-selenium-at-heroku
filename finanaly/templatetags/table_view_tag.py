from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]

@register.filter
def get_obj_attr(obj, attr):
    return getattr(obj, attr)