import $ from 'jquery';
window.$ = window.jQuery = $;
require('popper.js/dist/umd/popper');
require('bootstrap/dist/js/bootstrap');
require('./plugins/bootstrap-switch');
require('./plugins/nouislider.min');
require('./now-ui-kit');

import Swal from 'sweetalert2';
window.Swal = Swal;
window.swal = Swal;

require('./plugins/bootstrap-datepicker');
require('./messages');
