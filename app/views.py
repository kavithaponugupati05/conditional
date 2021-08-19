from django.shortcuts import render

# Create your views here.
def hai(request):
    d={'a':220,'b':530,'c':100}
    return render(request,'hai.html',d)
