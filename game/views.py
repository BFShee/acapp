from django.http import HttpResponse

def index(request):
	link1 = '<h1 style="text-align:center">术士之战</h1>'
	return HttpResponse(link1)
	
