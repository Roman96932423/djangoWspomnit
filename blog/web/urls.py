from django.urls import path
from django.views.generic import DetailView, ListView

from web.views import UserBlogView
from web.models import Post


urlpatterns = [
    # Strona główna
    path("", ListView.as_view(model=Post), name="home_page"),
    
    # Strona postów konkretnego użytkownika
    path('<int:pk>/', UserBlogView.as_view(), name='user_posts'),
    
    # Strona detalnej treści wskazanego posta
    path('post-detail/<int:pk>/', DetailView.as_view(model=Post), name='post_detail')
]
