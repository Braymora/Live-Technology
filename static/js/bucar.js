function buscar() {
    var input = document.getElementById('input-busqueda');
    var filter = input.value.toUpperCase();
    var table = document.querySelector('.tabla');
    var rows = table.getElementsByTagName('tr');

    for (var i = 0; i < rows.length; i++) {
        var tdNombre = rows[i].getElementsByTagName('td')[0];
        var tdApellido = rows[i].getElementsByTagName('td')[1];
        var tdCorreo = rows[i].getElementsByTagName('td')[2];

        if (tdNombre || tdApellido || tdCorreo) {
            var txtValueNombre = tdNombre.textContent || tdNombre.innerText;
            var txtValueApellido = tdApellido.textContent || tdApellido.innerText;
            var txtValueCorreo = tdCorreo.textContent || tdCorreo.innerText;

            if (txtValueNombre.toUpperCase().indexOf(filter) > -1 ||
                txtValueApellido.toUpperCase().indexOf(filter) > -1 ||
                txtValueCorreo.toUpperCase().indexOf(filter) > -1) {
                rows[i].style.display = '';
            } else {
                rows[i].style.display = 'none';
            }
        }
    }
}