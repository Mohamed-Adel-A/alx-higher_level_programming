window.onload = function() {
const url = "https://hellosalut.stefanbohacek.dev/";
$("INPUT#btn_translate").click(function() {
    lang = $("INPUT#language_code").val();
    full_url = url + "?lang=" + lang;
    $get(full_url, function(data) {
        $("DIV#hello").text(data.hello);
    });
});
}
