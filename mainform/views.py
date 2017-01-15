from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from menumanage.models import SysMenu


@login_required
def mainform(request):
    menus = SysMenu.objects.all()
    return render(request, 'mainform/index.html', context={
        "menus": menus
    })
