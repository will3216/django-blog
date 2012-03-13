from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from django.views.generic.simple import direct_to_template
from blog.models import Post
from django.contrib.syndication.views import Feed
import blog.archives.urls

class BlogFeed(Feed):
    title = "the blog"
    description = "Some stuff about stuff"
    link = "/blog/feed/"
    
    def items(self):
        return Post.objects.all().order_by("-created")[:2]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.body
    def item_link(self, item):
        return u"/blog/%d" % item.id

urlpatterns = patterns('blog.views',
    url(r'^$', ListView.as_view(
        #Change the [:2] in order to show more than two posts
        queryset=Post.objects.all().order_by("-created")[:2],
        template_name="blog.html")),
    url(r'^Overview/$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="overview.html")),
    url(r'^technical_drawings/$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="technical_drawings.html")),
    url(r'^safety/$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="safety.html")),
    url(r'^measuring/$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="measuring.html")),
    url(r'^materials/$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="materials.html")),
    url(r'^machining_and_tools/$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="machining_and_tools.html")),
    url(r'^(?P<pk>\d+)', DetailView.as_view(
        model=Post,
        template_name="post.html")),
    url(r'^archives/', ListView.as_view(
        #Change the [:2] in order to show more than two posts
        queryset=Post.objects.all().order_by("-created"),
        template_name="archives.html"))
    url(r'^2012/$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="2012.html")),
    url(r'^April/$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="April.html")),
    url(r'^March/$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="March.html")),
    url(r'^February/$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="February.html")),
    url(r'^January/$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="January.html")),
    url(r'^2011/$', ListView.as_view(
        queryset=Post.objects.all().order_by("-created"),
        template_name="2011.html")),
    url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
    url(r'^feed/$', BlogFeed()),
    url(r'^about/$', direct_to_template, {'template': 'about.html'}),
    url(r'^contact/$', direct_to_template, {'template': 'contact.html'}),
    url(r'^construction/$', direct_to_template, {'template': 'construction.html'}),
)
