var lightbox = {
	conf: {
		el: '#base-lightbox',
		box: '#base-lightbox-container',
		fadeInDelay: 250,
		fadeOutDelay: 250
	},
	mostrar: function(){
		$(this.conf.el).fadeIn(this.conf.fadeInDelay);
		$(this.conf.box).css({
			marginTop: - $(this.conf.box).height() / 2,
			marginLeft: - $(this.conf.box).width() / 2
		});
	},
	ocultar: function(){
		$(this.conf.el).fadeOut(this.conf.fadeOutDelay);
	}
};

function obtenerFecha(hora){
	var f = new Date(),
		day = f.getDate(),
		month = f.getMonth() + 1,
		year = f.getFullYear();
	if(day < 10) day = '0' + day;
	if(month < 10) month = '0' + month;
	var total = day + '-' + month + '-' + year;
	if(hora){
		var hora = f.getHours(),
			minutos = f.getMinutes(),
			segundos = f.getSeconds();
		if(hora < 10) hora = '0' + hora;
		if(minutos < 10) minutos = '0' + minutos;
		if(segundos < 10) segundos = '0' + segundos;
		total = total + ', ' + hora + ':' + minutos + ':' + segundos;
	}
	return total;
}

function recargarPagina(delay){
	setTimeout(function(){
		location.reload();
	}, delay);
}