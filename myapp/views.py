from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myapp_home(request):
    response = """
        <h1>Hello World</h1>
<h2>I am learning Django</h2>

"""
    return HttpResponse(response)
