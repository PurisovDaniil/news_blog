from django.contrib import admin
from .models import Post, Category, Comment, Image, Profile

# Register your models here.
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Post, PostAdmin)
admin.site.register(Category, PostAdmin)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Profile)