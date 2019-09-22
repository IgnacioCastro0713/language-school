import swal from 'sweetalert2';

const swalMaterial = swal.mixin({
  confirmButtonClass: 'btn btn-success',
  cancelButtonClass: 'btn btn-danger',
  buttonsStyling: false,
});

const toast = swal.mixin({
  toast: true,
  position: 'top',
  showConfirmButton: false,
  timer: 3000,
  showCloseButton: false
});

const confirmDelete = (e, name, url) => {
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
};

const deleteInShow = (e, name, url, index) => {
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
};

const deleteElement = (name, url, done, fail) => {
  swalMaterial({
    title: '¿Desea eliminar el elemento?',
    text: "Está apunto de eliminar el registro de " + name + ".",
    type: 'warning',
    showCancelButton: true,
    confirmButtonText: '<i class="now-ui-icons ui-1_check"></i>  Eliminar',
    cancelButtonText: '<i class="now-ui-icons ui-1_simple-remove"></i>  Cancelar',
  }).then((result) => {
    if (result.value) {
      $.ajax({
        data: {
          '_method': 'DELETE',
          csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val() || '',
        },
        type: 'post',
        url: url,
      }).done(done).fail(fail)
    }
  })
};

window.toast = toast;
window.swalMaterial = swalMaterial;
window.confirmDelete = confirmDelete;
window.deleteInShow = deleteInShow;
window.deleteElement = deleteElement;
