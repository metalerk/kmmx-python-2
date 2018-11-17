from django.views.generic import TemplateView
from .models import Post

class PostsView(TemplateView):
	template_name = 'posts.html'
	posts = Post.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(PostsView, self).get_context_data(*args, **kwargs)
		context.update({'posts': self.posts})
		return context

class PostDetailView(TemplateView):
	template_name = 'post_detail.html'

	def get_context_data(self, *args, **kwargs):
		context = super(PostDetailView, self).get_context_data(*args, **kwargs)
		post_id = self.kwargs.get('post_id', None)
		post_detail = Post.objects.get(id=post_id)
		context.update({'post_detail': post_detail})
		return context
