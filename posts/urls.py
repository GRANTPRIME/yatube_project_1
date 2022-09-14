from django.urls import path
from . import views

app_name = 'posts_list'
urlpatterns = [
    path('', views.index, name='posts_list'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts_list'),
]