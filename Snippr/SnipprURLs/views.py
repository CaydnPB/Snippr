from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import SnipprSnippet

def snippets(request):
    snippets = SnipprSnippet.objects.all()
    return render(request, 'projectboard/projects.html', {'projects': projects})

def singlesnippet(request, snippet_id):
    snippet = get_object_or_404(SnipprSnippet, pk=snippet_id)
    return JsonResponse(snippet)
    return JsonResponse({'message': 'Issue status updated successfully'})

    return render(request, 'projectboard/projectsdetail.html', {'project': project, 'issues_by_status': issues_by_status})
