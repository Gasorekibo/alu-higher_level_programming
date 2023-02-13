#!/usr/bin/node
$(document).ready(function () {
    $('DIV#add_item').click(function () {
        $('ul.my_list').prepend('<li>Item</li>');
    });
});