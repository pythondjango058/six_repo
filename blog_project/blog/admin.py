from django.contrib import admin
from blog.models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','published','created','updated','status']
    list_filter=('status','author','created','published')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='published'
    ordering=['status','published']
    prepopulated_fields={'slug':('title',)}
admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=['name','email','post','body','created','updated','active']
    list_filter=('active','created','updated')
    search_fields=('name','email','body')
admin.site.register(Comment,CommentAdmin)
