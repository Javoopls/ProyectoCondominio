from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='grupo')
def grupo(user, group_name):
    g = Group.objects.get(name=group_name)
    return True if g in user.groups.all() else False