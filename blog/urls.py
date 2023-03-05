from django.urls import path

from blog.views import (
    PostListView, 
    PostDetailView, 
    CategoryPostListView, 
    TagPostListView,
    SearchPostListView,
    CommentCreateView,
    ReplyCreateView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('category/<str:slug>/', CategoryPostListView.as_view(), name='category-post-list'),
    path('tag/<str:slug>/', TagPostListView.as_view(), name='tag-post-list'),
    path('search/', SearchPostListView.as_view(), name='search-post-list'),
    path('comment/<int:post_pk>/', CommentCreateView.as_view(), name='comment'),
    path('reply/<int:comment_pk>/', ReplyCreateView.as_view(), name='reply'),
]