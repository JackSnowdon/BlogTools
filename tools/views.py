from django.shortcuts import render

# Create your views here.

def toolshome(request):
    return render(request, "toolshome.html")