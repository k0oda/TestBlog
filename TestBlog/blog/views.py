from django.shortcuts import render
from .models import Post


class Home:

    @staticmethod
    def list_posts(request):
        posts = Post.objects.all()
        return render(request, 'blog/post_list.html', {'posts': posts})
