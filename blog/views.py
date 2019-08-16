from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm


class Home:

    @staticmethod
    def list_posts(request):
        posts = Post.objects.all().order_by('publication_date').reverse().order_by('publication_time')
        for post in posts:
            post.text_size = len(post.text)
            post.text = post.text[:200]
        current_date = timezone.localdate(timezone.now())
        return render(request, 'blog/post_list.html', {'posts': posts, 'current_date': current_date})

    @staticmethod
    def new_post(request):
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.Meta.model.publish(form)
                return redirect('list_posts')
        else:
            form = PostForm()
        return render(request, 'blog/new_post.html', {'form': form})

    @staticmethod
    def post_detail(request, primary_key=None):
        post = get_object_or_404(Post, pk=primary_key)
        return render(request, 'blog/post_detail.html', {'post': post})

    @staticmethod
    def edit_post(request, primary_key=None):
        post = get_object_or_404(Post, pk=primary_key)
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post_to_save = form.save(commit=False)
                post_to_save.publication_date = timezone.localdate(timezone.now())
                post_to_save.publication_time = timezone.localtime(timezone.now())
                post_to_save.save()
                return redirect('list_posts')
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/new_post.html', {'form': form})
