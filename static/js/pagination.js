var opcUrl = table;

const changePage = (obj, e) => {
  e.preventDefault();
  let page = $(obj).attr('href').split('?page=')[1];
  let param = $('#search').val();
  if (param !== "")
    opcUrl = search + '/' + param + '/';
  else
    opcUrl = table;
  $.ajax({
    url: opcUrl + '?page=' + page
  }).done(function (response) {
    $('#content').html(response);
    location.hash = page;
    $('html, body').stop().animate({
      scrollTop: $("#top").offset().top
    }, 250)
  })
};

var currentUrl = table;

const loadTable = (e, doSearch) => {
  e.preventDefault();
  let param = $('#search').val();
  if (doSearch && param !== "")
    currentUrl = search + '/' + param + '/';
  else
    currentUrl = table;
  $.ajax({
    url: currentUrl,
    method: 'get',
    csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val() || '',
  }).done(function (response) {
    currentUrl = search;
    $('#content').html(response);
    if (doSearch)
      location.hash = $('#search').val();
  })
};
