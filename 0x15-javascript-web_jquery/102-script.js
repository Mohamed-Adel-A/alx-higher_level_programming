const url = "https://hellosalut.stefanbohacek.dev/?lang=ja"
lang = $("INPUT#language_code").value
$("INPUT#btn_translate").click(function() {
    alert(lang)
});
