from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from .models import SnipprSnippet
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from decouple import config
from cryptography.fernet import Fernet, InvalidToken


SYMMETRIC_KEY = config("SYMMETRIC_KEY")
cipher_suite = Fernet(SYMMETRIC_KEY)

@method_decorator(csrf_exempt, name='dispatch')
def snippets(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        title = data.get('title', '')
        language = data.get('language', '')
        # code = data.get('code', '') - Unencrypted
        code = cipher_suite.encrypt(data.get('code', '').encode('utf-8'))
        snippet = SnipprSnippet.objects.create(title=title, language=language, code=code)
        return JsonResponse({'id': snippet.id, 'title': snippet.title, 'language': snippet.language})
    elif request.method == 'GET':
        snippets = SnipprSnippet.objects.all()
        snippet_list = [{'id': snippet.id, 'title': snippet.title, 'language': snippet.language, 'code': cipher_suite.decrypt(snippet.code).decode('utf-8')} for snippet in snippets]
        return JsonResponse(snippet_list, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})


@method_decorator(csrf_exempt, name='dispatch')
def singlesnippet(request, snippet_id):
    if request.method == 'GET':
        snippet = get_object_or_404(SnipprSnippet, pk=snippet_id)
        snippet_return = {'id': snippet.id, 'title': snippet.title, 'language': snippet.language, 'code': cipher_suite.decrypt(snippet.code).decode('utf-8')}
        return JsonResponse(snippet_return, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})

@method_decorator(csrf_exempt, name='dispatch')
def user(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email', '')
        password = make_password(data.get('password', ''))
        user = User.objects.create(username=email, password=password)
        return JsonResponse({'success': 'User created successfully'})
    elif request.method == 'GET':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email', '')
        password = data.get('password', '')
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                return JsonResponse({'id': user.id, 'username': user.username})
            else:
                return JsonResponse({'Error': 'Invalid login credentials'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'Error': 'User not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'})