import Swal from 'sweetalert2';
window.Swal = Swal;
window.swal = Swal;

require('./plugins/bootstrap-datepicker');
import { toast, swalMaterial, confirmDelete, deleteInShow, deleteElement } from './messages';