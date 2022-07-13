$(document).ready(function(){
    $("#doggobtn").click(function(){
        $.getJSON("https://random.dog/doggos", function(data){
            var rnd;
            rnd = Math.floor(Math.random()*data.length);
            $('#dog-img').attr('src', "https://random.dog/" + data[rnd]);
    });
    })
});