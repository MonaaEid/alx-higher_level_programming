$('document').ready(function () {
    $('INPUT#btn_translate').on('click', function () {
        $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang : $('INPUT#language_code').val() }, function (data, textStatus) {
            if (textStatus === 'success') {
                $('DIV#hello').text(data.hello);
            }
        });
    });
});
