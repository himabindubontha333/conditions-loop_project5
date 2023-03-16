from django.shortcuts import render

# Create your views here.
def conditions(request):
     d={'a':99,'b':999,'c':1999}
     return render(request,'conditions.html',context=d)

def loop(request):
    d={'name':'Kanna'}
    return render(request,'loop.html',d)
