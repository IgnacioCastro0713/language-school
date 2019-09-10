import $ from 'jquery';
import Swal from 'sweetalert2';

window.$ = window.jQuery = $;
window.Swal = Swal;
window.swal = Swal;

require('popper.js/dist/umd/popper');
require('bootstrap');
require('./plugins/bootstrap-switch');
require('./plugins/nouislider.min');
require('./plugins/bootstrap-datepicker');
require('./now-ui-kit');

import { toast, swalMaterial, confirmDelete, deleteInShow, deleteElement } from './messages';