from django.shortcuts import render
from .models import Room
# Create your views here.
#Front code


def rooms(request):
	details = Room.objects.all().filter(availibility=True)
	return render(request, 'room_lelo/home.html', {"details":details})