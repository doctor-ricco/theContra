from django.http import HttpResponse, HttpRequest

from common.auth import awriter_required, aget_user # type: ignore
from common.django_utils import arender

from .forms import ArticleForm

@awriter_required
async def dashboard(request: HttpRequest) -> HttpResponse:
    return await arender(request, 'writer/dashboard.html')

@awriter_required
async def create_article(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = await form.asave(commit = False)
            article.user = await aget_user(request)
            await article.asave()
            return HttpResponse('Article created successfully!')
    else:
        form = ArticleForm()

    context = {'create_article_form': form}
    return await arender(request, 'writer/create-article.html', context)