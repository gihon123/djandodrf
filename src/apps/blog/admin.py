from django.contrib import admin

# Register your models here.

from apps.blog.models import BlogModel


class BlogModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(BlogModel, BlogModelAdmin)