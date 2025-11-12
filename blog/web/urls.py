from django.urls import path

from web.views import HomeView, UserBlogView


urlpatterns = [
    path("", HomeView.as_view(), name="home_page"),
    path('<int:pk>', UserBlogView.as_view(), name='user_posts')
]
