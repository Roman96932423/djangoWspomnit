from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from web.models import Post


User = get_user_model()


class UserBlogView(ListView):
    model = Post
    template_name = 'globals/index.html'
    
    def get(self, request, pk, **kwargs):
        self.user = get_object_or_404(User, pk=pk)
        
        return super().get(request, **kwargs)
    
    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context.update({
            'title': f'Blog by: {self.user}',
			'user_name': self.user,
			'user_about': self.user.about_user,
            'user_image': self.user.user_image
		})
        
        return context
    
    