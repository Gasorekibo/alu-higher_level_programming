#!/usr/bin/node
$('document').ready(function () {
    $('input#btn_translate').click(function () {
      $.get('https://www.fourtonfish.com/hellosalut/?' + $.param({ lang: $('input#language_code').val() }), function (data) {
        $('div#hello').html(data.hello);
      });
    });
  });