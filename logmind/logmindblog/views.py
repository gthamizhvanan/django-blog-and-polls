from logmindblog.models import lmBlog, lmCategory
from django.shortcuts import render,get_object_or_404
from django.views.generic import View,TemplateView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.core.urlresolvers import reverse

class LogMindBlogClass(View):

	def get(self,request,slug):
			return render(request,'view_post.html', {
			'post' : get_object_or_404(lmBlog,slug=slug)
			})

	def post(self,request):
		if request.POST['txtBlogId']!='':
			blogedit = get_object_or_404(lmBlog,id=request.POST['txtBlogId'])
			#blogedit = lmBlog.objects.get(slug=request.POST['txtBlogId'])
			blogedit.blogtitle = request.POST['txtBlogTitle']
			blogedit.description = request.POST['txtDesc']
			blogedit.blogcategory_id = request.POST['txtCatId']
			blogedit.slug           = slugify(request.POST['txtBlogTitle'])
			#blogdetails = Blog(blogtitle=addlmblogTitle,description=addlmblogDesc,blogcategory_id=addlmblogCatId,slug=slug)
			blogedit.save()
			return HttpResponseRedirect(reverse('logmindblog:all'))
		else:
			addlmblogTitle = request.POST['txtBlogTitle']
			addlmblogDesc = request.POST['txtDesc']
			addlmblogCatId = request.POST['txtCatId']
			slug           = slugify(addlmblogTitle)
			addlmblog = lmBlog.objects.create(blogtitle=addlmblogTitle,description=addlmblogDesc,blogcategory_id=addlmblogCatId,slug=slug)
			addlmblog.save()
			return HttpResponseRedirect(reverse('logmindblog:view', args=(slug,)))

	def put(self,request,slug):
		p = get_object_or_404(lmBlog,slug=slug)
		blogedit = lmBlog.objects.get(slug=slug)
		blogedit.blogtitle = request.POST['txtBlogTitle']
		blogedit.description = request.POST['txtDesc']
		blogedit.blogcategory_id = request.POST['txtCatId']
		blogedit.slug           = slugify(request.POST['txtBlogTitle'])
		#blogdetails = Blog(blogtitle=addlmblogTitle,description=addlmblogDesc,blogcategory_id=addlmblogCatId,slug=slug)
		blogedit.save()
		return HttpResponseRedirect(reverse('logmindblog:view', args=(slug,)))

	# def delete(self,request,slug):
	# 	p = get_object_or_404(lmBlog,slug=slug) 
	# 	p.delete()
	# 	return HttpResponseRedirect(reverse('logmindblog:view', args=(slug,)))

class LogMindFormAddClass(TemplateView):	
	template_name = 'addblog.html'

class LogMindFormEditClass(TemplateView):
	def get(self,request,slug):
		return render(request,'editblog.html', {
			'post' : get_object_or_404(lmBlog,slug=slug)
			})

class LogMindFormAllClass(TemplateView):	
	template_name = 'index.html'
	def allblogs(self):
		return lmBlog.objects.all()

class LogMindFormDeleteClass(View):
	def get(self,request):
		lmBlog.objects.filter(pk=request.GET['id']).delete()
		return HttpResponseRedirect(reverse('logmindblog:all'))

	