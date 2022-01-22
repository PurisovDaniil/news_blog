from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('news/', views.news, name = 'news'),
    path('news/<slug:slug>', views.post_detail, name = 'post_detail_url'),
    path('categories/<slug:slug>', views.category_detail, name = 'category_detail_url'),
    path('search/', views.search_function, name = 'search_url'),
    path('register/', views.register, name = 'register'), 
    path('news/<slug:slug>/comment/', views.comment, name = 'comment'),
    path('sort/', views.sort, name = 'sort'),
    path('profile/', views.profile, name = 'profile_url'),
    path('profile/save_bg/', views.save_bg, name = 'save_bg'),
    path('users/<str:username>', views.user_detail, name='user_detail'),
]