from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$', views.campeones, name='campeones'),
	url(r'^(?P<slug>[-\w]+)/(?P<id>\d+)/$', views.campeon, name='campeon'),
]