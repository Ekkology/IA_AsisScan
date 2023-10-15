// Función para cargar dinámicamente la cámara
function cargarCamara() {
    var iframe = document.getElementById("cameraFrame");
    iframe.src = "http://192.168.137.32:8080/browserfs.html";
}

// Llama a la función para cargar la cámara cuando se carga la página
window.onload = cargarCamara;
