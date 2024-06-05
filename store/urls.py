from django.urls import path
from . import views


urlpatterns = [

    path('', views.main_page, name='main_page'),
    path('main/', views.main_page, name='main_page'),


    path('category/', views.category, name='category'),
    path('post/<slug:post_slug>/', views.post, name='post'),
    path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'),



        ]
handler404 = views.page_not_found