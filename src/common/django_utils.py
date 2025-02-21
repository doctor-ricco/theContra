"""
Common Django utils used by several other packages and
apps inside of this project.
"""

__all__ = (
    'AsyncFormMixin',
    'AsyncModelFormMixin',
    'AsyncViewT'
    'arender',
    'alogout',
)

from typing import Protocol

from django import forms

from asgiref.sync import sync_to_async
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

import django.contrib.auth as auth

class AsyncViewT(Protocol):
    async def __call__(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        ...



class AsyncFormMixin():
    @sync_to_async
    def ais_valid(self: forms.BaseForm): # type: ignore
        return self.is_valid()
    
    @sync_to_async
    def arender(self: forms.BaseForm): # type: ignore
        return self.render()
    

class AsyncModelFormMixin(AsyncFormMixin):
    @sync_to_async
    def asave(self: forms.BaseForm): # type: ignore
        return self.save()

async def arender(*render_args, **render_kargs) -> HttpResponse:
    @sync_to_async
    def sync_call_render() -> HttpResponse:
        return render(*render_args, **render_kargs)
    return await sync_call_render()

async def alogout(*render_args, **render_kargs):
    @sync_to_async
    def sync_call_logout():
        auth.logout(*render_args, **render_kargs)
    await sync_call_logout()