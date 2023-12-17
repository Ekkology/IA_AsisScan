const botonAdmin = document.getElementById('boton-admin');
const botonEst = document.getElementById('boton-est');
const botonDoc = document.getElementById('boton-doc');

const administrativos = document.getElementById('Administrativos');
const estudiantes = document.getElementById('Estudiantes');
const docentes = document.getElementById('Docentes');

const tipo = document.getElementById('tipo-tabla');

function esconderTodo(){
    administrativos.classList.add('ocultar')
    estudiantes.classList.add('ocultar')
    docentes.classList.add('ocultar') 
}

function mostrar(tabla){
    tabla.classList.remove('ocultar')
}

botonAdmin.addEventListener('click', () => {
    esconderTodo()
    mostrar(administrativos)
    tipo.textContent = 'Administrativos'
    
})
botonEst.addEventListener('click', () => {
    esconderTodo()
    mostrar(estudiantes)
    tipo.textContent = 'Estudiantes'
   
})

botonDoc.addEventListener('click',  () => { 
    esconderTodo();
    mostrar(docentes);
    tipo.textContent = 'Docentes';
    
})

// FUNCIONES PARA ACCIONES DE AÑADIR Y ELIMINAR 

// mostrar/ocultar el overlay
function abrirOverlay() {
    document.getElementById('overlay').style.display = 'block';
    mostrarCamposSegunRol(); //esto para que pueda cargar los campos del rol que esta por default al abrir el overlay
  }
  
  function cerrarOverlay() {
    document.getElementById('overlay').style.display = 'none';
  }
  
  function limpiarFormulario() {
    document.getElementById('formularioAñadir').reset();
  }
  
  // Llama a esta función al cargar la página para añadir el evento clic al botón Añadir
  document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('boton-anadir').addEventListener('click', function() {
      abrirOverlay();
      limpiarFormulario();
    });
  });
  
  // Agrega esta función para guardar los datos en la base de datos
  function guardarDatos() {
    // Obtener los valores de los campos del formulario
    var nuevoNombre = document.getElementById('nombre').value;
    var nuevoRol = document.getElementById('rol').value;
    var nuevaAsistencia = document.getElementById('asistencia').value;
    // falta tambien agregar el valor de la foto 
    // aqui hay que editar para que de acuerdo a los roles seleccionados se guarden en la BD 
    // Cierra el overlay después de guardar los datos
    cerrarOverlay();
  }

  //funciones para las opciones del combobox

  function mostrarCamposSegunRol() {
    var seleccion = document.getElementById("seleccionRol");
    var rolSeleccionado = seleccion.options[seleccion.selectedIndex].value;
  
    ocultarTodosLosCampos();
    // Mostrar los campos según el rol seleccionado
    if (rolSeleccionado === "admin") {
      mostrarCampos("camposAdmin");
    } else if (rolSeleccionado === "estudiante") {
      mostrarCampos("camposEstudiante");
    } else if (rolSeleccionado === "docente") {
      mostrarCampos("camposDocente");
    }
  }
  
  function ocultarTodosLosCampos() {
    // Ocultar todos los campos
    ocultarCampos("camposAdmin");
    ocultarCampos("camposEstudiante");
    ocultarCampos("camposDocente");
  }
  
  function mostrarCampos(idCampo) {
    // Mostrar los campos según el ID proporcionado
    document.getElementById(idCampo).style.display = "block";
  }
  
  function ocultarCampos(idCampo) {
    // Ocultar los campos según el ID proporcionado
    document.getElementById(idCampo).style.display = "none";
  }
  
  function mostrarCamposAdmin() {
    mostrarCampos("camposAdmin");
  }
  
  function mostrarCamposEstudiante() {
    mostrarCampos("camposEstudiante");
  }
  
  function mostrarCamposDocente() {
    mostrarCampos("camposDocente");
  }

  //funciones para hacer accionable las tablas cuando se toca el botón eliminar 

  /*document.getElementById('boton-eliminar').addEventListener('click', function() {
    hacerTablasSeleccionables();
    este es la version original de lo que esta abajo
  });*/
  var botonEliminar = document.getElementById('boton-eliminar');
  var eliminacionEnProceso = false;
  

  botonEliminar.addEventListener('click', function() {
    if (!eliminacionEnProceso) {
        hacerTablasSeleccionables();
        eliminacionEnProceso = true;
    }
  });

  function hacerTablasSeleccionables() {
    var tablas = document.querySelectorAll('.contenedor-tabla table');
  
    tablas.forEach(function(tabla) {
      var filas = tabla.getElementsByTagName('tbody')[0].getElementsByTagName('tr');
  
      for (var i = 0; i < filas.length; i++) {
        filas[i].addEventListener('click', function() {
          deseleccionarFilas(filas, this);
          //this.classList.toggle('seleccionada');
          //confirmarEliminar(this);
          this.classList.add('seleccionada');
          confirmarEliminar(this);
        });
      }
    });
  }
  
  function confirmarEliminar(fila) { // esto es para por si necesita hacer mod con la BD 
    // Aquí puedes mostrar el overlay de confirmación
    // Puedes acceder a los datos de la fila si es necesario
    var datosFila = obtenerDatosDeFila(fila);
    //confirmarEliminar(fila);
  
  }

  function confirmarEliminar(fila) {
    // Crear overlay de confirmación
    var overlay = document.createElement('div');
    overlay.className = 'confirmar-overlay';
    
    // Contenido del overlay
    var contenidoOverlay = document.createElement('div');
    contenidoOverlay.className = 'confirmar-contenido';
    
    // Mensaje de confirmación
    var mensaje = document.createElement('p');
    mensaje.textContent = '¿Estás seguro de que deseas eliminar este registro?';
    
    // Botones de confirmación
    var botonSi = document.createElement('button');
    botonSi.textContent = 'Sí';
    botonSi.addEventListener('click', function() {
      // Lógica para eliminar el registro
      eliminarRegistro(fila); // falta programarlo de acuerdo a lo de la BD
      // Cerrar overlay
      overlay.remove();
    });
    
    var botonNo = document.createElement('button');
    botonNo.textContent = 'No';
    botonNo.addEventListener('click', function() {
      // Cerrar overlay sin eliminar el registro
      fila.classList.remove('seleccionada');
      overlay.remove();
      
    });
  
    // Agregar elementos al overlay
    contenidoOverlay.appendChild(mensaje);
    contenidoOverlay.appendChild(botonSi);
    contenidoOverlay.appendChild(botonNo);
    overlay.appendChild(contenidoOverlay);
    
    // Agregar overlay al cuerpo del documento
    document.body.appendChild(overlay);
  }
  
  // funciones para eliminar el registro en las tablas
  function eliminarRegistro(fila) {
    // Aquí colocar la lógica para eliminar el registro BD
    // Puedes personalizar esta función según tus necesidades
  }

  function deseleccionarFilas(filas, filaActual) {
    for (var i = 0; i < filas.length; i++) {
      if (filas[i] !== filaActual) {
        filas[i].classList.remove('seleccionada');
      }
    }
  }

  // funciones para mostrar la foto al añadir otro registro 
  function subirFoto() {
    var inputFoto = document.getElementById('inputFoto');
    var contenedorProgreso = document.getElementById('contenedorProgreso');
    var nombreFoto = document.getElementById('nombreFoto');
    var barraProgreso = document.getElementById('barraProgreso');
  
    inputFoto.addEventListener('change', function () {
      var file = inputFoto.files[0];
      
      // Mostrar el contenedor de progreso
      contenedorProgreso.style.display = 'block';
      
      // Actualizar el nombre de la foto en el overlay
      nombreFoto.textContent = 'Nombre de la foto: ' + file.name;
  
      // Lógica para guardar la foto en la base de datos
      // (Debes implementar esta parte según tu backend)
  
      // Simulación de subida con un temporizador
      var progreso = 0;
      var interval = setInterval(function () {
        progreso += 10;
        barraProgreso.value = progreso;
  
        if (progreso >= 100) {
          // Limpia el intervalo cuando la carga se completa
          clearInterval(interval);
          // Oculta el contenedor de progreso
          contenedorProgreso.style.display = 'none';
        }
      }, 500);
    });
  
    // Limpiar el input para que se dispare el evento change si se selecciona la misma foto
    inputFoto.value = '';
  }
  
  // Resto de tu código...
  