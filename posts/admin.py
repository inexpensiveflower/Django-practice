from django.contrib import admin
from .models import Location, Post

class LocationAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

class PostAdmin(admin.ModelAdmin):
	list_display = ('subject', 'content', 'author', 'location')
	exclude = ('create_date',)

admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)