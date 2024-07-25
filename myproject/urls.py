from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


def home(request):  # Here request is Django WSGIRequest
    return HttpResponse("Hello World. I am learning django")  # return response object


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path("", include('myapp.urls')),  # This is an example of URL Chaining
    
]
