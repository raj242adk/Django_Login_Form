from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request,"blog/login.html")

def post(request):
    pass

def further_details(request):
    pass
