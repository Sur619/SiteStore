from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.loader import render_to_string

from store.models import Posts, Category, TagPost


from django.shortcuts import render
from .models import Posts

def main_page(request):
    posts = Posts.objects.filter(is_published=True)
    title = "Latest Games"
    return render(request, 'store/main_page.html', {'posts': posts, 'title': title})






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





def category_list(request):
    categories = Category.objects.all()
    return render(request, 'Store/category.html', {'categories': categories})

def category_games(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    games = category.posts_set.all()
    return render(request, 'Store/category_games.html', {'category': category, 'games': games})

























def page_not_found(request, exception):
    return HttpResponseNotFound(f"Not Found")
