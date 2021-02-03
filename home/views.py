from django.shortcuts import render, HttpResponse

# Create your views here.
def index (request):
    context = {
        "variable": "this is your username"
    }
    return render(request, 'index.html', context)
  
def home (request):
    return HttpResponse("hello iam saketh from class 9a1 ")