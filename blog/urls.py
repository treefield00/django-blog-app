from django.urls import path

from blog.views import PostListView, PostDetailView, CategoryPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('category/<str:slug>/', CategoryPostListView.as_view(), name='category-post-list'),
]