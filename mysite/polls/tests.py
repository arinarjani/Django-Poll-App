import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

# Create your tests here.

class QuestionMethodTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() should return False for questions whose 
		pub_date() is in the future
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		"""
		was_published_recently() should return False for question whose
		pub_date is older than one day
		"""
		time = timezone.now() - datetime.timedelta(days=30)
		old_question = Question(pub_date = time)
		self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		time = timezone.now() - datetime.timedelta(hours=1)
		recent_question = Question(pub_date = time)
		self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days):
		"""
		Creates a question with the given `question_text` and published
		the given number of `days` offset to now (negative for questions
		published in the past, positive for questions, that have yet
		to be published)
		"""
		time = timezone.now() + datetime.timedelta(days = days)
		return Question.objects.create(question_text=question_text, 
									   pub_date = time)

class QuestionViewsTests(TestCase):

	def test_index_view_with_no_question:
		"""
		If no question exists, an appropriate message should be displayed.
		"""
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No Polls are available")

self.assertQuerysetEqual(response.context['latest_question_list'], [])

	def test_index_view_with_a_past_question(self):
		"""
		
		"""