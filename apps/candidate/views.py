from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView as _LoginView
from django.contrib.auth.decorators import login_required
from django.core.exceptions import BadRequest

from django.core import serializers


from .models import Candidate


def candidate_list(request):
    data = {
        'candidates': Candidate.objects.all()
    }
    return render(request, 'election/candidate_list.html', context=data)


def candidate(request, pk):
    data = {
        'candidate': get_object_or_404(Candidate, pk=pk)
    }
    return render(request, template_name='election/candidate.html', context=data)


@login_required
def vote(request, candidate_id):

    user = request.user
    if user.voted_candidates.exists():
        raise BadRequest('Already voted')

    candidate = Candidate.objects.get(id=candidate_id)
    candidate.vote_count += 1
    candidate.voters.add(request.user)
    candidate.save()

    return redirect('candidate_list')


class LoginView(_LoginView):
    template_name = 'election/login.html'


def api_candidate_list(request):
    data = {
        'candidates': [
            {
                'id': 1,
                "name": 'Ram',
                'Party': 'UML'
            }
        ]
    }
    return JsonResponse(data=data)
