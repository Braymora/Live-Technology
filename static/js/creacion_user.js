document.addEventListener('DOMContentLoaded', function() {
    // Selecciona el botón de cancelar por su clase
    var cancelarBtn = document.querySelector('.cancelar_md');
    
    // Agrega un evento de clic al botón
    cancelarBtn.addEventListener('click', function() {
        // Obtiene la URL de la página de gestión de usuarios de los datos personalizados del botón
        var url = cancelarBtn.getAttribute('data-url');
        
        // Redirige al usuario a la página de gestión de usuarios
        window.location.href = url;
    });
});
