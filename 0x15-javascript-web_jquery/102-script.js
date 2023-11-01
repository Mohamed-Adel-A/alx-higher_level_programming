window.onload = function() {
const url = "https://hellosalut.stefanbohacek.dev/"
$("INPUT#btn_translate").click(function() {
    lang = $("INPUT#language_code").val()
    alert(lang)
});
}
