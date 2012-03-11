from blog.models import Post
from django.shortcuts import render_to_response

def tagpage(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    item = {'posts':posts, 'tag':tag, 'hmm':"wah"}
    return render_to_response("tagpage.html", item)
