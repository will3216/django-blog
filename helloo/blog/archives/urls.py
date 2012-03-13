from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from blog.models import Post


urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
        #Change the [:2] in order to show more than two posts
        queryset=Post.objects.all().order_by("-created"),
        template_name="archives.html")),
    url(r'^2012$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="2012.html")),
    url(r'^April$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="April.html")),
    url(r'^March$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="March.html")),
    url(r'^February$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="February.html")),
    url(r'^January$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="January.html")),
    url(r'^2011$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="2011.html")),
)