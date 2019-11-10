from django.shortcuts import render
from .models import Room
# Create your views here.
#Front code


def rooms(request):
	try:
		search=request.GET['search']
	except:
		search=""
	if search:
		details = Room.objects.all().filter(availibility=True,location__icontains=search)
	else:		
		details = Room.objects.all().filter(availibility=True)
	return render(request, 'room_lelo/home.html', {"details":details})