document.addEventListener("DOMContentLoaded", function () {
    var imagePaths = ["../pokemon/img/01.png", "../pokemon/img/02.png","../pokemon/img/03.png","../pokemon/img/04.png", "../pokemon/img/05.png",
        "../pokemon/img/06.png", "../pokemon/img/07.png", "../pokemon/img/08.png", "../pokemon/img/09.png", "../pokemon/img/10.png",
        "../pokemon/img/11.png", "../pokemon/img/12.png", "../pokemon/img/13.png", "../pokemon/img/14.png", "../pokemon/img/15.png",
        "../pokemon/img/16.png", "../pokemon/img/17.png", "../pokemon/img/18.png", "../pokemon/img/19.png", "../pokemon/img/20.png",
        "../pokemon/img/pikachu.png"];

    var container = document.getElementById("raindrop-container");

    function createRaindrop() {
        var raindrop = document.createElement("div");
        raindrop.classList.add("raindrop");

        var randomImagePath = imagePaths[Math.floor(Math.random() * imagePaths.length)];
        raindrop.style.backgroundImage = "url('" + randomImagePath + "')";

        raindrop.style.left = Math.random() * window.innerWidth + "px";
        raindrop.style.top = "-30px";

        container.appendChild(raindrop);

        var animationDuration = Math.random() * 6 + 1;
        raindrop.style.animation = "fallAnimation " + animationDuration + "s linear infinite";

        setTimeout(function () {
            container.removeChild(raindrop);
        }, animationDuration * 1000);
    }

    var rainInterval = setInterval(createRaindrop, 200);
});


