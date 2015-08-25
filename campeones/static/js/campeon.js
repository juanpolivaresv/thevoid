var csrftoken = Cookies.get('csrftoken');

function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings){
        if(!csrfSafeMethod(settings.type) && !this.crossDomain){
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

var campeon = {
	api: {
		conf: {
			region: 'las',
			apiKey: '93ad4cc0-b04d-4dee-b2c2-a1fe49d63d85'
		}
	},
	datos: {
		boton: {
			el: '#campeon-boton-datos',
			texto: function(texto, activado){
				$(this.el).html(texto);
				if(activado) this.activar();
				else this.desactivar();
			},
			activar: function(){
				$(this.el).addClass('activado');
			},
			desactivar: function(){
				$(this.el).removeClass('activado');
			}
		},
		obtener: function(championId){
			$.ajax({
				url: 'https://global.api.pvp.net/api/lol/static-data/' + campeon.api.conf.region + '/v1.2/champion/' + championId + '?champData=lore&api_key=' + campeon.api.conf.apiKey,
				type: 'GET',
				data: {},
				dataType: 'json',
				success: function(json){
					campeon.datos.enviar(json);
					recargarPagina(3000);
				},
				error: function(){
					campeon.datos.boton.texto('Error', false);
					recargarPagina(1500);
				}
			});
		},
		enviar: function(datosObtenidos){
			datosObtenidos['ultima_actualizacion'] = obtenerFecha(true);
			$.ajax({
				url: templateData.url,
				type: 'POST',
				data: JSON.stringify(datosObtenidos),
				dataType: 'json',
				contentType: 'application/json; charset=utf-8',
				success: function(){
				},
				failure: function(errMsg){
		        	console.log('errMsg');
		    	}
			});
		}
	},
	nav: {
		elementos: {
			opcion: undefined,
			contenido: undefined
		},
		seleccionar: function(opcion){
			if(campeon.nav.elementos.opcion != undefined){
				$(campeon.nav.elementos.opcion).css('color', 'rgb(205, 205, 205)');
				$(campeon.nav.elementos.opcion).removeClass('selected').addClass('nav-option');
			}
			if(campeon.nav.elementos.contenido != undefined){
				campeon.nav.ocultar(campeon.nav.elementos.contenido);
			}
			campeon.nav.elementos.opcion = opcion;
			$(campeon.nav.elementos.opcion).removeClass('nav-option').addClass('selected');
			for(i = 0; i < $('.campeon-datos-contenido').length; i++){
				var el = $('.campeon-datos-contenido')[i];
				if($(el).data('content') == $(campeon.nav.elementos.opcion).data('content')){
					campeon.nav.elementos.contenido = el;
					campeon.nav.mostrar(el);
				}
			}
		},
		mostrar: function(contenido){
			$(contenido).css('display', 'block');
		},
		ocultar: function(contenido){
			$(contenido).css('display', 'none');
		}
	}
};

$('#campeon-boton-datos').click(function(){
	if(!$(this).hasClass('activado')) return false;
	if($(this).data('status') == 'obtener'){
		campeon.datos.boton.texto('Obteniendo...', false);
	}
	else {
		campeon.datos.boton.texto('Actualizando...', false);
	}
	campeon.datos.obtener(templateData.championId);
});

$('.nav-option').click(function(){
	if(campeon.nav.elementos.opcion == this) return false;
	campeon.nav.seleccionar(this);
});

$(document).ready(function(){
	$('.nav-option').mouseover(function(){
		if(campeon.nav.elementos.opcion == this) return false;
		$('.selected').css('color', 'rgb(105, 105, 105)');
	});
	$('.nav-option').mouseout(function(){
		if(campeon.nav.elementos.opcion == this) return false;
		$('.selected').css('color', 'rgb(205, 205, 205)');
	});
});