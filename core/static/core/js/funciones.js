function mostrarSaludo(){

    fecha = new Date();
    hora = fecha.getHours();

    if(hora >= 0 && hora < 12){
        texto = "Buenos Días, ";
    } else if(hora >=12 && hora < 18){
        texto = "Buenas Tardes, ";
    } else{
        texto = "Buenas Noches, "
    }
    document.getElementById('saludo').innerHTML = texto;
}

$(function(){

    $(".dropdown-menu li a").click(function(){

      $(".btn:first-child").text($(this).text());
      $(".btn:first-child").val($(this).text());

   });

});