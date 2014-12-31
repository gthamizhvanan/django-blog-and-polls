from django.conf.urls import patterns, url

from logmindblog import views

urlpatterns = patterns('',
	url(r'^blog/',views.LogMindFormAllClass.as_view(), name='all'),
	url(r'^view/(?P<slug>[^\.]+)',views.LogMindBlogClass.as_view(), name='view'),
	url(r'^postblog/',views.LogMindBlogClass.as_view(), name='postblog'),
	url(r'^addblog',views.LogMindFormAddClass.as_view(), name = 'addblog'),
	url(r'^putblog/',views.LogMindBlogClass.as_view(), name='putblog'),
	url(r'^editblog/(?P<slug>[^\.]+)',views.LogMindFormEditClass.as_view(), name = 'editblog'),
	url(r'^deleteblog/',views.LogMindFormDeleteClass.as_view(), name = 'deleteblog'),
)