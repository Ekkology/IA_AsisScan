// Agregar el evento click a la imagen
const imgContainer = document.querySelector(".logo-container2");
imgContainer.addEventListener("click", async () => {
    try {
        // Descargar la imagen
        const response = await fetch("http://192.168.137.32:8080/photo.jpg");

        // Verificar si la solicitud fue exitosa (código de respuesta 200)
        if (response.status === 200) {
            // Obtener el contenido de la imagen como Blob
            const imageBlob = await response.blob();

            // Crear una URL a partir de la imagen descargada
            const imageURL = URL.createObjectURL(imageBlob);

            // Crear un nuevo elemento <img> para mostrar la imagen
            const imgElement = document.createElement("img");
            imgElement.src = imageURL;
            imgElement.style.width = "600px";
            imgElement.style.height = "600px";

            // Agregar el elemento <img> al contenedor de imágenes existente
            const fotoContainer = document.querySelector(".foto");
            fotoContainer.innerHTML = ""; // Limpiar el contenedor antes de agregar el nuevo elemento
            fotoContainer.appendChild(imgElement);

            // Desvanecer la imagen después de 5 segundos
            imgElement.style.transition = "opacity 5s";
            imgElement.style.opacity = 1;
            setTimeout(() => {
                imgElement.style.opacity = 0;
                // Liberar la URL creada para la imagen
                URL.revokeObjectURL(imageURL);
            }, 5000);
        } else {
            console.error("Error al descargar la imagen:", response.status);
        }
    } catch (error) {
        console.error("Error en la solicitud:", error);
    }
});
