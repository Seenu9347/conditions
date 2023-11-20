from django.shortcuts import render

# Create your views here.
def somu(request):
    d={'a':10,'b':50,'c':30}
    return render(request,'somu.html',d)
