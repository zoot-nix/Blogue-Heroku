from blogueApp.models import Category
from django.urls import path
# from django.conf.urls import url
from . import views
from .views import AddCommentView, HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView,ContactView, learn

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('subscribe/', ContactView.as_view(), name='subscribe-newsletter'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='edit-post'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='delete-post'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
    path('category/<str:cats>/', CategoryView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='comment'),
    path('learn/', views.learn, name='learn')
]
