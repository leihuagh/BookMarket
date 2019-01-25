from django import forms
from comments.models import Comments


# форма для добавления комментариев без кастомного тега
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments

        fields = [
            'user',
            'comments',
            'content_type',
            'object_id',
        ]

        widgets = {
            'user': forms.HiddenInput(),
            'content_type': forms.HiddenInput(),
            'object_id': forms.HiddenInput()
        }
