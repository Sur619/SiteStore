from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [

    path('', views.main_page, name='main_page'),
    path('main/', views.main_page, name='main_page'),


 #   path('category/', views.category, name='category'),
    path('post/<slug:post_slug>/', views.post, name='post'),
    path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LogoutView.as_view(), name='login'),
    path('register/', auth_views.LogoutView.as_view(), name='register'),


    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.category_games, name='category_games'),




        ]
handler404 = views.page_not_found


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)