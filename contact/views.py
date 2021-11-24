from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'contact.html')

def terminos(request):
    
    return render (request,'Terminos.html')