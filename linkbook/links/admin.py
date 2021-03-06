from django.contrib import admin
from django import forms
from .models import Link, Book, Comment

class LinkAdmin(admin.ModelAdmin):
	list_display = ('title', 'url', 'user', 'date')
	ordering = ['date']

class BookAdmin(admin.ModelAdmin):
	readonly_fields = ('get_links',)
	list_display = ('title', 'user', 'date', 'get_links')
	ordering = ['date']

	def get_links(self, obj):
		links = "\n".join(link.url for link in obj.link_set.all())
		return links

class CommentAdmin(admin.ModelAdmin):
	list_display = ('link', 'user', 'text', 'date')
	ordering = ['date']


admin.site.register(Link, LinkAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Comment, CommentAdmin)