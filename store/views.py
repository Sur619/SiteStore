from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.loader import render_to_string

from store.models import Posts, Category, TagPost


def main_page(request):
    posts = Posts.objects.filter(is_published=True)
    posts_category = Category.objects.all()
    categories = Category.objects.filter(id__in=posts.values('category_id'))
    data = {
        'post': posts,
        'posts_category': posts_category,
        'categories': categories,

    }
    return render(request, 'store/main_page.html', data)


def category(request):
    categories = Category.objects.all()
    posts = Posts.objects.all()
    data = {
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'store/includes/categories.html', data)


def post(request, post_slug):
    tags = get_object_or_404(Posts, slug=post_slug)
    data = {
        'post': post,
    }
    return render(request, 'store/post.html', data)


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = Posts.objects.filter(tags=tag, is_published=True)

    data = {
        'title': f'Tag: {tag.tag}',
        'posts': posts,
        'post_selected': None,

    }

    return render(request, 'store/main_page.html', data)


def page_not_found(request, exception):
    return HttpResponseNotFound(f"Not Found")
