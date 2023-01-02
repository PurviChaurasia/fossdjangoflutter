from django.shortcuts import render, HttpResponse

# Create your views here.
def hello_django(request):
    print("Request Recieved")
    return HttpResponse("Hello Django")
    
