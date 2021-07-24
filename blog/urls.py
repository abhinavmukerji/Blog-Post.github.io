from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,AddCommentView
from . import views #. represents current directory

urlpatterns=[path('',PostListView.as_view(),name='blog-home'),
path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
path('post/<int:pk>',PostDetailView.as_view(),name='post-detail'),
path('post/new/',PostCreateView.as_view(),name='post-create'),
path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
path('post/<int:pk>/comment/',AddCommentView.as_view(),name='add-comment'),
path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
path('about/',views.about,name='blog-about'),]
                # ^^ here you'll have to leave it blank instead of admin if you want to see homepage on opening the site
                       #^^ in the second parameter, we'll provide the view which will handle the logic at Home Page

#<app>/<model>_<viewtype>.html-->by default searching is done in this url when PostListView.as_view() is written

