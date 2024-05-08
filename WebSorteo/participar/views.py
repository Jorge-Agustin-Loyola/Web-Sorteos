from django.shortcuts import render

# Create your views here.
def participar(request):
    return render(request,"participar/participar.html")