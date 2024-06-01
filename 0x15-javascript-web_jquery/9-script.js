// A JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.
// Your script must work when it is imported from the <head> tag
// The translation of “hello” must be displayed in the HTML tag DIV#hello

$(document).ready(function() {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
        $('#hello').text(data.hello);
    });
});
