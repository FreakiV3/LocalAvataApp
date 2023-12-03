// script.js

function loadAnimation() {
    fadeInText("main-title", 1000);
    fadeInImage("kawaii-img", 2000);
    fadeInText("credit-text", 1500);
    setTimeout(function () {
        runCurlScript();
    }, 10000); // Délai de 10 secondes pour l'animation
}


// Ajoutez une nouvelle fonction pour exécuter le script Curl
function runCurlScript() {
    // Exécutez le script Curl pour obtenir les informations
    fetch('/run_curl_script')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.blob();  // Traitement en tant que blob (flux binaire)
        })
        .then(blob => {
            // Redirection vers la route "/panel"
            window.location.replace("/panel");
        })
        .catch(error => {
            console.error('Error during script execution:', error);
        });
}

function fadeInText(elementId, duration) {
    var element = document.getElementById(elementId);
    element.style.opacity = 0;
    var startTime = null;

    function fadeIn(currentTime) {
        if (!startTime) startTime = currentTime;
        var progress = currentTime - startTime;
        element.style.opacity = progress / duration;
        if (progress < duration) {
            requestAnimationFrame(fadeIn);
        }
    }

    requestAnimationFrame(fadeIn);
}

function fadeInImage(elementId, duration) {
    var element = document.getElementById(elementId);
    element.style.opacity = 0;
    var startTime = null;

    function fadeIn(currentTime) {
        if (!startTime) startTime = currentTime;
        var progress = currentTime - startTime;
        element.style.opacity = progress / duration;
        if (progress < duration) {
            requestAnimationFrame(fadeIn);
        }
    }

    requestAnimationFrame(fadeIn);
}

// Reste du script...

// Ajoutez d'autres fonctions d'animation et de logique au besoin
