// A JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
// All movie titles must be list in the HTML tag UL#list_movies
$(document).ready(function() {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
        data.results.forEach(function(film) {
            $('#list_movies').append('<li>' + film.title + '</li>');
        });
    });
});
