from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.create_post, name='create_post'),
    path('comment/<int:pk>/like/', views.like_comment, name='like_comment'),
    path('signup/', views.signup, name='signup'),
]
