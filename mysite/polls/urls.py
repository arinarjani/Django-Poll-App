from django.conf.urls import url

from . import views

# namespace
app_name = 'polls'

# these are going to be passed to the question_id param in polls.views
# except for urlpatterns[0], that is simply the request param
urlpatterns = [
	# ex: /polls/
	url(r'^$', views.index, name='index'),
	# ex: /polls/5/
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name = 'detail'),
	# ex: /polls/5/results/
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name = 'results'),
	# ex: /polls/5/vote/
	url(r'(?P<question_id>[0-9]+)/vote/$', views.vote, name = 'vote')
]