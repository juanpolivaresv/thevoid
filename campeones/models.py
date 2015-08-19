from django.db import models
from django.template import defaultfilters

class Rol(models.Model):
	nombre = models.CharField(help_text='Escribe el nombre del rol', max_length=64)
	descripcion = models.CharField(help_text='Escribe la descripcion del rol', max_length=512)

	def __unicode__(self):
		return self.nombre


class Campeon(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(help_text='Escribe el nombre del campeon', max_length=64)
	descripcion = models.CharField(help_text='Escribe la descripcion del campeon', max_length=256)
	rol = models.ForeignKey(Rol, related_name='rol')
	rol_secundario = models.ForeignKey(Rol, related_name='rol_secundario', blank=True, null=True)
	slug = models.SlugField(max_length=256, editable=False)
	avatar = models.ImageField(upload_to='campeones/static/img/avatar')
	splash = models.ImageField(upload_to='campeones/static/img/splash')

	def __unicode__(self):
		return '%s - %s' % (self.nombre, self.descripcion)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = defaultfilters.slugify(self.descripcion)
			super(Campeon, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return '/campeones/%s/%i/' % (self.slug, self.id)

	def get_avatar_url(self):
		return self.avatar.url[10:]

	def get_splash_url(self):
		return self.splash.url[10:]
