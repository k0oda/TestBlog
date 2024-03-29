"""TestBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.list_posts, name='list_posts'),
    path('post/new/', Home.new_post, name='new_post'),
    path('post/<int:primary_key>/', Home.post_detail, name='post_detail'),
    path('post/<int:primary_key>/edit/', Home.edit_post, name='edit_post'),
]
