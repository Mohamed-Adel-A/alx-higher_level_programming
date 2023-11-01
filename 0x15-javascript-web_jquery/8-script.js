const url = "https://swapi-api.alx-tools.com/api/films/?format=json"
$.get(url, function(data, status) {
    for (item in data.results)
        $("UL#list_movies").append("<li>" + item.title + "</li>");
});
