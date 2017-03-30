from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1 style=\"color: red; font-family: sans-serif;\">Hello, world.  You're at the polls index.</h1>")