from blog.models import Post
from django import template
register=template.Library()

@register.simple_tag(name='vishwa_tag')
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('blog/latest_posts123.html')
def show_latest_posts(count=3):
    latest_posts=Post.objects.order_by('-published')[:count]
    return {'latest_posts':latest_posts}

from django.db.models import Count
@register.inclusion_tag('blog/latest_comments123.html')
def get_most_commented_posts(count=5):
    latest_comments=Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
    return {'latest_comments':latest_comments}
