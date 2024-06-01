// A JavaScript script that fetches the character name from the given URL and displays it in the DIV#character using jQuery.
$(document).ready(function() {
    $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
        $('#character').text(data.name);
    });
});
