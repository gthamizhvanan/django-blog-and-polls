# from django.conf.urls import patterns,url,include

# from polls import views

# urlpatterns = patterns('',
# 	url(r'^$',views.index,name='index'),
# 	url(r'^(?P<questionid>\d+)/$', views.question_details, name = 'question_details'),
# 	url(r'^(?P<questionid>\d+)/results/$',views.question_results, name = 'question_results'),
# 	url(r'^(?P<questionid>\d+)/vote/$',views.vote_details, name = 'vote_details'),
# )

# from django.conf.urls import patterns, url

# from polls import views

# urlpatterns = patterns('',
#     url(r'^$', views.IndexView.as_view(), name='index'),
#     url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='question_details'),
#     url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='question_results'),
#     #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote_details'),
#     url(r'^(?P<question_id>\d+)/vote/$', views.VoteView.as_view(), name='vote_details'),
# )



from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='question_details'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='question_results'),
    #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote_details'),
    url(r'^(?P<question_id>\d+)/vote/$', views.VoteView.as_view(), name='vote_details'),
)

