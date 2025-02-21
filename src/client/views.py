from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from common.auth import aclient_required # type: ignore

@aclient_required
async def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, 'client/dashboard.html')
