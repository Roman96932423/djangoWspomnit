from django.urls import path
from django.views.generic import DetailView, ListView, UpdateView

from web.views import UserBlogView
from web.models import Post


urlpatterns = [
    # Strona główna
    path("", ListView.as_view(model=Post), name="home_page"),
    
    # Strona postów konkretnego użytkownika
    path('<int:pk>/', UserBlogView.as_view(), name='user_posts'),
    
    # Strona detalnej treści wskazanego posta
    path('post-detail/<int:pk>/', DetailView.as_view(model=Post), name='post_detail'),
    
    # Strona do edytowanie posta
    path('post-update/<int:pk>/', UpdateView.as_view(
        model=Post,
        fields=('title', 'teaser', 'content', 'header_image'),
        success_url='/post-detail/{id}'
        ), name='post_update')
]
