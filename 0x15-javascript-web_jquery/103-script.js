$('document').ready(function () {
    $('INPUT#btn_translate').on('click', function () {
        translate();
    });

    $('INPUT#language_code').on('keypress', function (event) {
        if (event.which === 13) {
            translate();
            alert('you entered the Enter key');
        }
    });

    function translate() {
        $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang : $('INPUT#language_code').val() }, function (data, textStatus) {
            if (textStatus === 'success') {
                $('DIV#hello').text(data.hello);
            }
        });
    }
});