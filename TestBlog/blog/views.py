from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


class Home:

    @staticmethod
    def list_posts(request):
        posts = Post.objects.all()
        for post in posts:
            post.text_size = len(post.text)
            post.text = post.text[:200]
        return render(request, 'blog/post_list.html', {'posts': posts})

    @staticmethod
    def new_post(request):
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('list_posts')
        else:
            form = PostForm()
        return render(request, 'blog/new_post.html', {'form': form})

    @staticmethod
    def post_detail(request, primary_key=None):
        post = get_object_or_404(Post, pk=primary_key)
        return render(request, 'blog/post_detail.html', {'post': post})
