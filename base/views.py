from django.shortcuts import render
from random import shuffle
from campeones.models import Campeon

def home(request):
	campeones = Campeon.objects.all()
	x = [i for i in range(len(campeones))]
	shuffle(x)
	campeon_al_azar = campeones[x[0]]
	template = 'home.html'
	return render(request, template, {'campeon_al_azar': campeon_al_azar})
