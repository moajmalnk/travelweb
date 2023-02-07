from django.shortcuts import render
from .models import Place, Team


def display(request):
    obj = Place.objects.all()
    team = Team.objects.all()
    return render(request, "index.html", {'display': obj, 'display_team': team})
