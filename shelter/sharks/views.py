from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Shark

def home(request):
    return render(request, "home.html")

def about(request):
    return HttpResponse("<h1>About</h1>")

def list(request):
    sharks = Shark.objects.all()
    return render(request, "shark-list.html", { "sharks": sharks })

@login_required
def show(request, id):
    shark = get_object_or_404(Shark, pk=id)
    return render(request, 'shark-show.html', { "shark": shark })
    