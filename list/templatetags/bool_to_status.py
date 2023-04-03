from django import template

register = template.Library()


@register.simple_tag
def bool_to_status(completed: bool) -> str:
    return "Done" if completed else "Not done"
