from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""
		Return the last five publised question
		(not includeing those set to be published in the future)
		"""
		return Question.objects.filter(
				pub_date_lte=timezone.now()
			).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except:
		# Redisplay the question voting form
		return render(request, 'polls/detail.html', {
				'question': question,
				'error_message': 'You didn\'t select a choice.',
			})
	else:
		selected_choice.votes = F('votes') + 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing 
		# with Post data.  This prevents data from being posted twice if a 
		# user hits the back button.
		# reverse(url_name) simply uses the url_name in urls.py for the url 
		# url redirection.  It does not reverse anything.
		return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

