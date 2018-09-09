const swalMaterial = swal.mixin({
    confirmButtonClass: 'btn btn-success',
    cancelButtonClass: 'btn btn-danger',
    buttonsStyling: false,
});

const toast = swal.mixin({
    toast: true,
    position: 'top',
    showConfirmButton: false,
    timer: 2000,
    showCloseButton: true
});

function confirmDelete(e, name, url) {
    e.preventDefault();
    deleteElement(name, url, function () {
        toast({
            title: 'Eliminado correctamente.',
            type: 'success'
        });
        loadTable(e, false);
    }, function () {
        toast({
            title: 'No se ha podido eliminar el elemento.',
            type: 'error'
        });
        loadTable(e, false);
    });
}

function deleteInShow(e, name, url, index) {
    e.preventDefault();
    deleteElement(name, url, function () {
        toast({
            title: 'Eliminado correctamente.',
            type: 'success'
        });
        window.location.replace(index);
    }, function () {
        toast({
            title: 'No se ha podido eliminar el elemento.',
            type: 'error'
        });
    });
}

function deleteElement(name, url, done, fail) {
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    swalMaterial({
        title: '¿Desea eliminar el elemento?',
        text: "Está apunto de eliminar el registro de "+csrftoken+".",
        type: 'warning',
        showCancelButton: true,
        confirmButtonText: '<i class="now-ui-icons ui-1_check"></i>  Eliminar',
        cancelButtonText: '<i class="now-ui-icons ui-1_simple-remove"></i>  Cancelar',
    }).then((result) => {
        if (result.value) {
            $.ajaxSetup({
                headers: {
                    'X-CSRF-TOKEN': csrftoken
                }
            });
            $.ajax({
                data: {
                    '_method' : 'DELETE',
                    csrfmiddlewaretoken: csrftoken,
                },
                type: 'post',
                url: url,
            }).done(done).fail(fail)
        }
    })
}