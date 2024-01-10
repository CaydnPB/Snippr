from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import SnipprSnippet
from django.views import View
import json

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
def snippets(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        title = data.get('title', '')
        language = data.get('language', '')
        code = data.get('code', '')
        snippet = SnipprSnippet.objects.create(title=title, language=language, code=code)
        return JsonResponse({'id': snippet.id, 'title': snippet.title, 'language': snippet.language, 'code': snippet.code})
    else:
        snippets = SnipprSnippet.objects.all()
        snippet_list = [{'id': snippet.id, 'title': snippet.title, 'language': snippet.language, 'code': snippet.code} for snippet in snippets]
        return JsonResponse(snippet_list, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
def singlesnippet(request, snippet_id):
    snippet = get_object_or_404(SnipprSnippet, pk=snippet_id)
    snippet_return = {'id': snippet.id, 'title': snippet.title, 'language': snippet.language, 'code': snippet.code}
    return JsonResponse(snippet_return, safe=False)