$(document).ready(function(){

    var formError;

    $("#error-nombre-reg").hide();
    $("#error-correo-reg").hide();
    $("#error-contrasena-reg").hide();
    $("#error-rcontrasena-reg").hide();
    

    $("#registro").submit(function(){

        formError = false;
        
        if($("#nombre").val().trim().length == 0){
            $("#error-nombre-reg").show();
            formError = true;
        }
        else{
            $("#error-nombre-reg").hide();
        }

        if($("#correo").val().trim().length == 0){
            $("#error-correo-reg").show();
            formError = true;
        }
        else{
            $("#error-correo-reg").hide();
        }

        if($("#contrasena").val().length == 0){
            $("#error-contrasena-reg").show();
            formError = true;
        }
        else{
            $("#error-contrasena-reg").hide();
        }

        if(($("#contrasena").val() != $("#rcontrasena").val()) || ($("#rcontrasena").val().length == 0)){
                $("#error-rcontrasena-reg").show();
                formError = true;
        }
        else{
            $("#error-rcontrasena-reg").hide();
        }
        
        if(formError){
            event.preventDefault();
            alert("Revisa los campos");
        }
    });

    $("#error-correo-log").hide();
    $("#error-contrasena-log").hide();

    $("#login").submit(function(){
        
        formError = false;
        
        if($("#correo-log").val().trim().length == 0){
            $("#error-correo-log").show();
            formError = true;
        }
        else{
            $("#error-correo-log").hide();
        }

        if($("#contrasena-log").val().length == 0){
            $("#error-contrasena-log").show();
            formError = true;
        }
        else{
            $("#error-contrasena-log").hide();
        }
        
        if(formError){
            event.preventDefault();
            alert("Revisa los campos");
        }
    });
});