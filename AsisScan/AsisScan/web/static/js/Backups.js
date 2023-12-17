function mostrarInformacion() {
    // Aquí puedes hacer una solicitud AJAX para recuperar los datos de la base de datos.
    // Supongamos que los datos se obtienen en formato JSON.
    // Reemplaza esta parte con tu lógica para obtener los datos reales.

    // Ejemplo de datos de prueba en formato JSON
    const datosDePrueba = [
      {
        nombre: "Juan",
        apellido: "Pérez",
        cedula: "123456789",
        correo: "juan@example.com",
        fotos: ["ruta_foto1.jpg", "ruta_foto2.jpg"],
      },
      {
        nombre: "María",
        apellido: "López",
        cedula: "987654321",
        correo: "maria@example.com",
        fotos: ["ruta_foto3.jpg"],
      },
      // Agrega más datos de prueba aquí
    ];

    const backupItems = document.querySelector(".backup-items");

    // Limpia cualquier contenido existente en .backup-items
    backupItems.innerHTML = "";

    // Itera a través de los datos y crea elementos HTML para mostrarlos
    datosDePrueba.forEach((registro) => {
      const backupItem = document.createElement("div");
      backupItem.className = "backup-item";

      const backupInfo = document.createElement("div");
      backupInfo.className = "backup-info";

      // Crea elementos de párrafo para mostrar los datos
      const nombreP = document.createElement("p");
      nombreP.textContent = "Nombre: " + registro.nombre;
      backupInfo.appendChild(nombreP);

      const apellidoP = document.createElement("p");
      apellidoP.textContent = "Apellido: " + registro.apellido;
      backupInfo.appendChild(apellidoP);

      const cedulaP = document.createElement("p");
      cedulaP.textContent = "Cedula: " + registro.cedula;
      backupInfo.appendChild(cedulaP);

      const correoP = document.createElement("p");
      correoP.textContent = "Correo Electrónico: " + registro.correo;
      backupInfo.appendChild(correoP);

      const photosCarousel = document.createElement("div");
      photosCarousel.className = "photos-carousel";

      // Itera a través de las fotos y crea elementos de imagen
      registro.fotos.forEach((foto, index) => {
        const photo = document.createElement("div");
        photo.className = "photo";
        const img = document.createElement("img");
        img.src = foto;
        img.alt = "Foto " + (index + 1);
        photo.appendChild(img);
        photosCarousel.appendChild(photo);
      });

      backupItem.appendChild(backupInfo);
      backupItem.appendChild(photosCarousel);
      backupItems.appendChild(backupItem);
    });
}
