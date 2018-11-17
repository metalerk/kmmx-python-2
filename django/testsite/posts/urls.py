from django.conf.urls import url
from .views import PostsView, PostDetailView

app_name = 'posts'

urlpatterns = [
    url(r'^$', PostsView.as_view(), name='all'),
    url(r'^detail/(?P<post_id>([a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}))/$', PostDetailView.as_view(), name='detail'),

]
