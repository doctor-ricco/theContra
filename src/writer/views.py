from django.http import HttpResponse, HttpRequest

from common.auth import awriter_required # type: ignore
from common.django_utils import arender

@awriter_required
async def dashboard(request: HttpRequest) -> HttpResponse:
    return await arender(request, 'writer/dashboard.html')