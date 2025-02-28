from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.exceptions import ObjectDoesNotExist

from .models import Subscription
from writer.models import Article
from common.django_utils import arender
from common.auth import aclient_required # type: ignore
from common.auth import aget_user

PlanChoices = Subscription.PlanChoices


@aclient_required
async def dashboard(request: HttpRequest) -> HttpResponse:
    user = await aget_user(request)
    try:
        subscription = await Subscription.objects.aget(user = user, is_active = True)
        plan = PlanChoices(subscription.plan)
        subscription_plan = 'premium' if plan == PlanChoices.PREMIUM else 'standard'
    except ObjectDoesNotExist:
        subscription_plan = 'none'

    context = {'subscription_plan': subscription_plan}
    return await arender(request, 'client/dashboard.html', context)

@aclient_required
async def browse_articles(request: HttpRequest) -> HttpResponse:
    user = await aget_user(request)
    try:
        subscription = await Subscription.objects.aget(user = user, is_active = True)
        has_subscription = True
        plan = PlanChoices(subscription.plan)
        subscription_plan = 'premium' if plan == PlanChoices.PREMIUM else 'standard'
        if plan == PlanChoices.STANDARD:
            articles = Article.objects.filter(is_premium = False).select_related('user')
        else:
            articles = Article.objects.all().select_related('user')
    except ObjectDoesNotExist:
        has_subscription = False
        subscription_plan = 'none'
        articles = []

    context = {
        'has_subscription': has_subscription, 
        'articles': articles,
        'subscription_plan': subscription_plan,
    }
    return await arender(request, 'client/browse-articles.html', context)