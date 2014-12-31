from django.contrib import admin

from logmindblog.models import lmBlog, lmCategory

class lmBlogAdmin(admin.ModelAdmin):
	exclude = ['posteddate']
	prepopulated_fields = {'subtitle':('title',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'catSlug':('title',)}

admin.site.register(lmBlog)
admin.site.register(lmCategory)
# Register your models here.
