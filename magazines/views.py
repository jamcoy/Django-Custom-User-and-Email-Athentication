from django.shortcuts import render
from .models import Magazine
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def all_magazines(request):
    magazines = Magazine.objects.all()
    return render(request, "magazines/magazines.html", {"magazines": magazines})
