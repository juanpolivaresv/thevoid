from django.db import models
from django.template import defaultfilters
from django.conf import settings

class Rol(models.Model):
	nombre = models.CharField(help_text='Escribe el nombre del rol', max_length=64)
	descripcion = models.CharField(help_text='Escribe la descripcion del rol', max_length=512)

	def __unicode__(self):
		return self.nombre


class Campeon(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(help_text='Escribe el nombre del campeon', max_length=64)
	descripcion = models.CharField(max_length=256, default='Sin datos de Riot Games', editable=False)
	rol = models.ForeignKey(Rol, related_name='rol')
	rol_secundario = models.ForeignKey(Rol, related_name='rol_secundario', blank=True, null=True)
	slug = models.SlugField(max_length=256, editable=False)
	splash = models.ImageField(upload_to='campeones/static/img/splash')
	lore = models.TextField(editable=False, default='')
	actualizado = models.BooleanField(default=False, editable=False)
	ultima_actualizacion = models.CharField(max_length=512, default='Nunca', editable=False)

	def __unicode__(self):
		return '%s - %s' % (self.nombre, self.descripcion)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = defaultfilters.slugify(self.nombre)
			super(Campeon, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return '/campeones/%s/%i/' % (self.slug, self.id)

	def get_splash_url(self):
		return self.splash.url[10:]

	def get_champion_id(self):
		return settings.CHAMPIONS_ID[self.nombre]
