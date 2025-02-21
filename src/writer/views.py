from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from common.auth import awriter_required # type: ignore


@awriter_required
async def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, 'writer/dashboard.html')