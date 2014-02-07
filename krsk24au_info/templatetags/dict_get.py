from django import template

register = template.Library()

@register.filter
def key(d, key_name):
    if key_name in d:
        return d[key_name]
    else:
        return ''
    # return d.get(key, 'asd')