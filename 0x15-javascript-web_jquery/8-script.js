const url = "https://swapi-api.alx-tools.com/api/films/?format=json"
$.get(url, function(data) {
    res = data.results
    len = res.length
    for (let i = 0; i < len ; i++){
        $("UL#list_movies").append("<li>" + res[i].title + "</li>");
    }
});
