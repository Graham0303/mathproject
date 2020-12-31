from django.shortcuts import render

# Create your views here.
def addnumbers(request):
    context = {}
    return render(request, 'calculations/addnumbers.html', context)

def addnumbersresult(request):
    context = {}
     
    return render(request, 'calculations/addnumbersresult.html', context)    