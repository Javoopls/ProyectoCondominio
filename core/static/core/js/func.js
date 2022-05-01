function today(){
    x = new Date();
    var months = new Array(12);
    months[0] = "Ene.";
    months[1] = "Feb.";
    months[2] = "Mar.";
    months[3] = "Abr.";
    months[4] = "May.";
    months[5] = "Jun.";
    months[6] = "Jul.";
    months[7] = "Ago.";
    months[8] = "Sep.";
    months[9] = "Oct.";
    months[10] = "Nov.";
    months[11] = "Dic.";
    var r = months[x.getMonth()];
    var date = r + " " + x.getDate() + ", " + x.getFullYear();
    document.getElementById('t').innerHTML = date;
};

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