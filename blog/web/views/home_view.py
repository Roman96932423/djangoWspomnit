from django.views.generic import ListView

from web.models import Post


class HomeView(ListView):
    template_name = 'index.html'
    model = Post
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Home Romana xD'
        
    #     return context
