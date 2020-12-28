$(document).ready(function () {
    $('#order_place').hide();
    $('#order_table').hide();
    $('#addNewItem').click(function () {
        $('#order_place').show();
         $('#order_table').hide();
    });
    $('#close').click(function () {
        $('#order_place').hide();
        $('#addNewItem').show();
        $('#order_table').show();
    });
});

$('#saveItems').click(function () {
    let id = $('#order_place').val();
    let name = $('#name').val();
    let csrfMiddleWareToken = $("[name=csrfmiddlewaretoken]")[0].value;
    let status = true;


    if (name === "") {
        $("#name").addClass("is-invalid");
        $("#nameError").html(strings.Name_Error).show();
        status = false;
    }

    window.open("/kite_login/?trading_symbol=name");

});

