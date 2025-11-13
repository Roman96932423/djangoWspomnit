from django.urls import path

from web.views import HomeView, UserBlogView, PostDetailView


urlpatterns = [
    # Strona główna
    path("", HomeView.as_view(), name="home_page"),
    
    # Strona postów konkretnego użytkownika
    path('<int:pk>/', UserBlogView.as_view(), name='user_posts'),
    
    # Strona detalnej treści wskazanego posta
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post_detail')
]
