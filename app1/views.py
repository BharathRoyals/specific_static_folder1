from django.shortcuts import render

# Create your views here.
def specific_static(request):
    return render(specific_static,'specific_static.html')
