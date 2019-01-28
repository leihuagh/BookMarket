from django import template
from django.contrib.contenttypes.models import ContentType
from ..models import Comments

register = template.Library()


@register.inclusion_tag('comments/comments.html', takes_context=True)
def comments(context, obj, next='/'):
    ct = ContentType.objects.get_for_model(obj)

    # список комментариев для объекта
    comments = Comments.objects.filter(
        content_type=ct,
        object_id=obj.pk
    )

    # context
    return {
        'ct': ct.pk,
        'obj_id': obj.pk,
        'comments': comments,
        'next': next
    }
