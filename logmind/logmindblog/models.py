from django.db import models
from django.db.models import permalink


class lmBlog(models.Model):
	blogtitle    = models.CharField(max_length=100,unique=True)
	slug         = models.SlugField(max_length=100,unique=True)
	description  = models.TextField()
	posteddate   = models.DateField(db_index=True,auto_now_add=True)
	blogcategory = models.ForeignKey('logmindblog.lmCategory')

	def __str__(self):
		return self.blogtitle

	# @permalink
	# def get_absolute_url(self):
	# 	return ('view_blog_post_list',None,{'slug',self.slug})

class lmCategory(models.Model):
	catTitle = models.CharField(max_length=100,unique=True)
	slug  = models.SlugField(max_length=100,unique=True)

	def __unicode__(self):
		return '%s' % self.catTitle

	@permalink
	def get_absolute_url(self):
		return ('view_cat_post_list',None,{'slug',self.slug})
# Create your models here.
