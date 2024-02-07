$('document').ready(function () {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, textStatus) {
        if (textStatus === 'success') {
            $('DIV#hello').append(data.hello);
        }
    })
})
