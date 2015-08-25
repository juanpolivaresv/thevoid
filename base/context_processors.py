from django.conf import settings
from campeones.models import Campeon

def datos_globales(request):
	numero_de_campeones = len(Campeon.objects.all())
	numero_de_campeones_con_datos = len(Campeon.objects.filter(actualizado=True))

	if numero_de_campeones_con_datos == 0:
		numero_de_campeones_con_datos = 'Ninguno'
	elif numero_de_campeones_con_datos == numero_de_campeones:
		numero_de_campeones_con_datos = 'Todos'

	primer_campeon_registrado = Campeon.objects.earliest('id')
	ultimo_campeon_registrado = Campeon.objects.latest('id')
	return {
		'datos_globales': {
			'version': settings.VERSION,
			'ultima_actualizacion': settings.ULTIMA_ACTUALIZACION,
			'numero_de_campeones': numero_de_campeones,
			'numero_de_campeones_con_datos': numero_de_campeones_con_datos,
			'primer_campeon_registrado': primer_campeon_registrado,
			'ultimo_campeon_registrado': ultimo_campeon_registrado,
		}
	}
