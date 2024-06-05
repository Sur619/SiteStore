from store.models import TagPost
from django import template

register = template.Library()


@register.inclusion_tag('store/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.all()}
