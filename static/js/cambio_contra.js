$(document).ready(function() {
    // Función para manejar el envío del formulario
    $('#cambio-password-form').submit(function(event) {
        event.preventDefault(); // Evitar el envío del formulario predeterminado

        // Obtener los datos del formulario
        var formData = $(this).serialize();

        // Realizar la petición AJAX
        $.ajax({
            type: 'POST',
            url: '/cambio/contraseña/admin/{{ user.id }}/', // Corregir la URL aquí
            data: formData,
            success: function(response) {
                if (response.success) {
                    // Mostrar mensaje de éxito y redirigir después de un tiempo
                    showSuccessMessage('La contraseña se ha cambiado correctamente.');
                    setTimeout(function() {
                        window.location.href = '/gestoruser/'; // Corregir la URL aquí
                    }, 2000);
                } else {
                    // Mostrar mensaje de error en caso de falla
                    showErrorModal(response.error_message);
                }
            },
            error: function(xhr) {
                // Mostrar mensaje de error en caso de error de la petición
                console.error(xhr.status + ": " + xhr.responseText);
                showErrorMessage('Error al cambiar la contraseña. Por favor, intenta de nuevo.');
            }
        });
    });

    // Al hacer clic en el botón "Cambiar Contraseña", mostrar el modal
    $('#cambio-password-form button[type="submit"]').click(function(event) {
        event.preventDefault();
        $('#errorModal').modal('show');
    });
});

// Función para mostrar un mensaje de error en el modal
function showErrorModal(errorMessage) {
    $('#errorModalBody').html('<p>' + errorMessage + '</p>');
}

// Función para mostrar un mensaje de error en la página
function showErrorMessage(errorMessage) {
    $('.error-message').html(errorMessage).show();
}

// Función para mostrar un mensaje de éxito en la página
function showSuccessMessage(successMessage) {
    $('.success-message').html(successMessage).show();
}


