from django.shortcuts import redirect, render
from .models import *
from .forms import *
    

def main(request):
    content = {
        
    }
    return render(request, 'checking/main.html', content)

