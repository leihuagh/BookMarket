from django.shortcuts import render
from django.views.generic.base import RedirectView
from django.views.generic import CreateView
from django.contrib.contenttypes.models import ContentType
from .forms import CommentsForm
from django.urls import reverse_lazy

from .models import Comments

# Create your views here.


# вью для добавления комментария через кастомный тег
class CommentsAdd(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        next = self.request.POST.get('next', '/')
        ct_id = self.request.POST.get('ct_id')
        obj_id = self.request.POST.get('obj_id')
        comments = self.request.POST.get('comments')
        user = self.request.user
        if ct_id and obj_id and comments:
            ct = ContentType.objects.get_for_id(ct_id)
            comments, created = Comments.objects.get_or_create(
                user=user,
                comments=comments,
                content_type=ct,
                object_id=obj_id,
                defaults={
                    'user': user,
                    'comments': comments,
                    'content_type': ct,
                    'object_id': obj_id,
                }
            )
        return next


# вью для добавления комментария без кастомного тега
# доделать правильный редирект
class CommentCreate(CreateView):
    template_name = 'products/prod-view-base.html'
    model = Comments
    form_class = CommentsForm
    success_url = reverse_lazy('products:book-prod-list')