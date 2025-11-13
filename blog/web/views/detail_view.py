from django.views.generic import DetailView

from web.models import Post


class PostDetailView(DetailView):
    model = Post
    template_name = 'globals/post_detail.html'
    