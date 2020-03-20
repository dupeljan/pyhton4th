from django.contrib import admin
from .models import Post, Author, Comment
# Register your models here.

class PostInstanceInline(admin.StackedInline):
	model = Comment
	extra = 0

class PostModeAdmin(admin.ModelAdmin):
	list_display = ['title','content','timestamp','updated',"post_likes"]
	list_display_links = ['content']
	list_filter = ['timestamp']
	inlines = [PostInstanceInline]
	ordering = ['-timestamp']
	#fields=('title',)
	#exclude = ('likes',)
	class Meta:
		model = Post

class AuthorModelAdmin(admin.ModelAdmin):
	list_display = ['first_name','last_name','email']
	list_filter = ['last_name']
	ordering= ['last_name','first_name']
	class Meta:
		model = Author

class CommentModelAdmin(admin.ModelAdmin):
	list_display = ['comment_text','comment_article']
	class Meta:
		model = Comment

admin.site.register(Post, PostModeAdmin)
admin.site.register(Author,AuthorModelAdmin)
admin.site.register(Comment,CommentModelAdmin)
