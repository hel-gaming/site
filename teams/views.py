from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.exceptions import ObjectDoesNotExist
from .models import Team
from .models import User


def index(request):
    teams_list = Team.objects.all()
    context = { 'teams_list': teams_list }
    return render(request, 'teams/index.html', context)

def detail(request, teamid):
    try:
        name = Team.objects.get(id=teamid).name
        response = 'Team: %s <br>' % name
        response += 'Members: <br>'
        users = User.objects.filter(team__name=name)
        for username in users:
            response += '  * %s <br>' % username
    except ObjectDoesNotExist:
        response = 'fuck you'

    return HttpResponse(response)

