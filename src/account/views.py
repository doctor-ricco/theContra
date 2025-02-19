from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

async def home(request: HttpRequest) -> HttpResponse:
    """..."""
    return render(request, 'account/home.html')

async def register(request: HttpRequest) -> HttpResponse:
    """..."""
    return render(request, 'account/register.html')

async def login(request: HttpRequest) -> HttpResponse:
    """..."""
    return render(request, 'account/login.html')

# Create your views here.