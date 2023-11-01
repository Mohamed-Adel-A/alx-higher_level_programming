window.onload = function() {
const url = "https://hellosalut.stefanbohacek.dev/?lang=ja"
$("INPUT#btn_translate").click(function() {
    lang = $("INPUT#language_code").value
    alert(lang)
});
}
