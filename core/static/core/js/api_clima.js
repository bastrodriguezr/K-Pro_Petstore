$(document).ready(function(){
    $("#weather").hide();

    var lat;
    var longit;
    var city_name;
    var temp;
    var country_name;
    var weather_description;
    var iconcode;
    var iconurl;
    var apiKey = "5dd765a29b95b2e058dfd9f33a1dbd0d";
    var lang = "es"

    if(("geolocation" in navigator)){
        $("#weather").show();
        navigator.geolocation.getCurrentPosition(showcityname);

        function showcityname(position){
            lat = position.coords.latitude;
            longit = position.coords.longitude;

            $.getJSON("http://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + longit + "&lang=" + lang + "&units=metric" + "&appid=" + apiKey, 
            function(data){

                city_name = data["name"];
                country_name = data["sys"]["country"];
                weather_description = data["weather"][0]["description"];
                temp = data["main"]["temp"];

                iconcode = data["weather"][0]["icon"];
                iconurl = "http://openweathermap.org/img/w/" + iconcode + ".png";
                $('#wicon').attr('src', iconurl);

                $("#cityname").html(city_name + " &#40;" + country_name + "&#41; ");
                $(".temp").html(temp + "ºC");

            });
        }
    }
});