$('document').ready(function () {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
        if (textStatus === 'success') {
            for (const movie of data.results) {
                $('UL#list_movies').append('<li>' + movie.title + '</li>');
            }
        };
    });
});
