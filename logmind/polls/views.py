from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import View
from django.template import RequestContext, loader
from polls.models import Choice, Question

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'all_latest_question'

	def get_queryset(self):
		"Last Five Questions"
		return Question.objects.order_by('-pub_date')[:2]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

# def vote(request,question_id):
# 	p = get_object_or_404(Question, pk=question_id)
# 	try:
# 		selected_choice = p.choice_set.get(pk=request.POST['radChoice'])
# 	except(KeyError, Choice.DoesNotExist):
# 		return render(request,'polls/detail.html', {
# 		'question':p,
# 		'error_message':"You didn't select a choice.",
# 		})
# 	else:
# 		selected_choice.votes += 1
# 		selected_choice.save()
# 	return HttpResponseRedirect(reverse('polls:question_results', args=(p.id,)))

# def results(request,questionid):
# 	question = get_object_or_404(Question,pk=question_id)
# 	return render(request,'polls/results.html',{'question':question})

class VoteView(View):

	def post(self,request,question_id):
		p = get_object_or_404(Question, pk=question_id)
		try:
			selected_choice = p.choice_set.get(pk=request.POST['radChoice'])
		except(KeyError, Choice.DoesNotExist):
			return render(request,'polls/detail.html', {
			'question':p,
			'error_message':"You didn't select a choice.",
			})
		else:
			selected_choice.votes += 1
			selected_choice.save()
		return HttpResponseRedirect(reverse('polls:question_results', args=(p.id,)))

	# def get(request,questionid):
	# 	return HttpResponse('Your Question is : %s' % questionid)

	# def question_results(request,questionid):
	# 	results_content = 'Your Question Result is : %s'
	# 	return HttpResponse(results_content % questionid)

	# def get(request):
	# 	all_latest_question = Question.objects.order_by('-pub_date')[:5]
	# 	template = loader.get_template('polls/index.html')
	# 	context = RequestContext(request,{'all_latest_question':all_latest_question})
	# 	return render(request,'polls/index.html',context)



	

# def detail(request,questionid):
# 	try:
# 		question = get_object_or_404(Question,pk=questionid)
# 	except Question.DoesNotExist:
# 		raise Http404
# 	return render(request,'polls/detail.html',{'question':question})

# def index(request):

# 	all_latest_question = Question.objects.order_by('-pub_date')[:5]
# 	template = loader.get_template('polls/index.html')
# 	context  = RequestContext(request,{'all_latest_question':all_latest_question})
# 	return render(request,'polls/index.html',context)
	#output               = ', '.join([p.question_text for p in all_latest_question])
	#return HttpResponse(template.render(context))
	#return HttpResponse('Hello World, I am a poll index !')


def question_details(request,questionid):
	return HttpResponse('Your Question is : %s' % questionid)

def question_results(request,questionid):
	results_content = 'Your Question Result is : %s'
	return HttpResponse(results_content % questionid)

def vote_details(request,questionid):
	return HttpResponse('Your Voting For This Question : %s ' % questionid)


# Create your views here.
