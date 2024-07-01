from django.http import HttpResponse
from django.shortcuts import render

def demo(request):
    print("welcome to Demo!")
    return render(request, "index.html")