from django.contrib import admin
from .models import Author, Post

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('nickname', 'email', 'nationality')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at', 'updated_at', 'author_email')

	def author_email(self, obj):
		return obj.author.email
