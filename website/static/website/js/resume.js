
const validateCard = (e) => {
    const reg = new RegExp('^[0-9]*$');
    let value = e.target.value;

    if(!reg.test(value)){
        $('#card').val(value.substring(0, value.length - 1));
    }
    if(value.length == 16){
        $('#card').prop("disabled", "true");
    }
};

const validateCVV = (e) => {
    const reg = new RegExp('^[0-9]*$');
    let value = e.target.value;

    if(!reg.test(value)){
        $('#code').val(value.substring(0, value.length - 1));
    }
    if(value.length == 3){
        $('#code').prop("disabled", "true");
    }
};

const validateMonth = (e) => {
    const reg = new RegExp('^[0-9]*$');
    let value = e.target.value;

    if(!reg.test(value)){
        $('#month').val(value.substring(0, value.length - 1));
    }
    if(parseInt(value) > 12 || parseInt(value) < 0){
        $('#month').val('');
    }
};

const validateYear = (e) => {
    const reg = new RegExp('^[0-9]*$');
    let value = e.target.value;

    if(!reg.test(value)){
        $('#year').val(value.substring(0, value.length - 1));
    }
    if(parseInt(value) > 99 || parseInt(value) < 0){
        $('#year').val('');
    }
};

const validatePay = (e) => {
    if($('#card').val().length != 16){
        e.preventDefault();
        alert("Por favor ingrese los 16 digitos de su tarjeta");
    }
    if($('#code').val().length != 3){
        e.preventDefault();
        alert("Por favor ingrese el código de seguridad");
    }
    if($('#month').val().length != 2){
        e.preventDefault();
        alert("Por favor ingrese el mes en formato de 2 numeros. Ej: 03");
    }
    if($('#year').val().length != 2){
        e.preventDefault();
        alert("Por favor ingrese el año en formato de 2 numeros.");
    }
}

$('#card').on('keyup', (e) => validateCard(e));
$('#code').on('keyup', (e) => validateCVV(e));
$('#month').on('keyup', (e) => validateMonth(e));
$('#year').on('keyup', (e) => validateYear(e));
$('#pay').on('submit', (e) => validatePay(e));