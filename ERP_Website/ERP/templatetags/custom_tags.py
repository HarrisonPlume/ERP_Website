from django import template

register = template.Library()

@register.filter
def get_dynamic_value(obj, attr):
    """
    Safely get the attribute from the object using the dynamic attribute name (attr).
    Works for both dictionaries (with .get()) and model instances (with getattr()).
    """
    if isinstance(obj, dict):
        return obj.get(attr)
    else:
        return getattr(obj, attr, None)