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

var datosDeCampeon = {
	misDatos: {
		nombre: 'testNombre',
		descripcion: 'testDescripcion'
	},
	enviarDatos: function(){
		$.ajax({
		    type: "POST",
		    url: "/campeones/the-void-burrower/6/",
		    data: JSON.stringify(this.misDatos),
		    contentType: "application/json; charset=utf-8",
		    dataType: "json",
		    success: function(data){alert(data);},
		    failure: function(errMsg) {
		        alert(errMsg);
		    }
		});
	}
};
