from django.shortcuts import render

def post(request):
	return render(request, 'blog/post.html', {})
# Create your views here.
