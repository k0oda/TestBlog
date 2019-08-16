from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Автор'})
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Название поста'})
        self.fields['text'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Текст'})

        try:
            if kwargs['instance']:
                self.fields['author'].widget.attrs.update({'readonly': ''})
        except KeyError:
            pass

    class Meta:
        model = Post
        exclude = ('publication_date', 'publication_time')
