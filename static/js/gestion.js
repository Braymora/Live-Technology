document.addEventListener("DOMContentLoaded", function() {
    const btnsEliminar = document.querySelectorAll(".eliminar");
    const btnsModificar = document.querySelectorAll(".modificar");

    btnsEliminar.forEach(btn => {
        const modalEliminar = document.getElementById(btn.dataset.id);
        const cancelarEliminar = modalEliminar.querySelector(".cancelar");

        btn.addEventListener("click", function() {
            modalEliminar.style.display = "block";
        });

        cancelarEliminar.addEventListener("click", function() {
            modalEliminar.style.display = "none";
        });
    });

    btnsModificar.forEach(btn => {
        const modalModificar = document.getElementById(btn.dataset.id);
        const cancelarModificar = modalModificar.querySelector(".cancelar_md");

        btn.addEventListener("click", function() {
            modalModificar.style.display = "block";
        });

        cancelarModificar.addEventListener("click", function() {
            modalModificar.style.display = "none";
        });
    });
});


