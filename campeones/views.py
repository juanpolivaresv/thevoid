import json
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from .models import Campeon

def campeones(request):
	campeones = Campeon.objects.order_by('nombre')
	template = 'campeones.html'
	return render_to_response(template, {'campeones': campeones})

def campeon(request, slug, id):
	if request.method == 'POST':
		try:
			data = json.loads(request.body)
			Campeon.objects.filter(slug=slug, id=id).update(nombre=data['nombre'], descripcion=data['descripcion'])
		except:
			raise Http404()

	campeon = get_object_or_404(Campeon, slug=slug, id=id)
	template = 'campeon.html'
	return render_to_response(template, {'campeon': campeon})
