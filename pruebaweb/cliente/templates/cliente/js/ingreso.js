function obtenerDatos(){
    console.log("cats")
     var userName = document.getElementById("Email1").value
     var pasword = document.getElementById("Password1").Value;
    
     document.nombreObtenido.value = userName
     document.paswordObtenida.value = pasword
}

var nombreObtenido;
var paswordObtenida;

var boton = document.getElementById("boton");
boton.onclick = obtenerDatos;