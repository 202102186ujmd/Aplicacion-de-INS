from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    try:
        return field.as_widget(attrs={"class": css_class})
    except AttributeError:
        # Si field no tiene el método as_widget, devuelve el field sin modificaciones
        return field
