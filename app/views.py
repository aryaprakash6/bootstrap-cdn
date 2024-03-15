from django.shortcuts import render

# Create your views here.
def carousel(request):
    return render(request, 'carousel.html')
def alert(request):
    return render(request, 'alert.html')
def toast(request):
    return render(request, 'toast.html')