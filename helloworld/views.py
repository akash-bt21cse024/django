from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    developed_by="Akash Kumar"
    mentors=[
        'akash','sahil','aayushman','tikam'
    ]
    context = {
        "developer": developed_by,
        'mentors': mentors
    }
    response = render(request,'helloworld/index.html', context )
    # response = HttpResponse("hii akash")
    return response     