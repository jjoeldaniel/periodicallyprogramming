// Dark Mode is off by default
window.onload = init;
let dark = false;

function init() {
    let element = document.getElementById("dark-mode-button");
    element.addEventListener("click", dark_mode);

    if (localStorage.getItem("dark_mode") === null) {
        localStorage.setItem("dark_mode", "false");
    }
    
    if (localStorage.getItem("dark_mode") === "true") {
        dark = true;
    }
    else if (localStorage.getItem("dark_mode") === "false") {
        dark = false;
    }

    // initialize dark mode
    if (dark) {
        document.body.classList.toggle("projects-dark-mode")
        document.getElementById("dark-mode-button").src= "https://github.com/jjoeldaniel/resume/blob/main/img/sun.png?raw=true";
        for (let i = 0; i < buttons.length; i++) {
            buttons[i].style.color = "#FFFFFF"; 
        }
    }

    console.log("page ready");
}

// Toggle Dark Mode
function dark_mode() {
    document.body.classList.toggle("projects-dark-mode")
    let buttons = document.getElementsByClassName("btn");

    // to light
    if (dark) {
        dark = false;
        localStorage.setItem("dark_mode", "false");

        document.getElementById("dark-mode-button").src= "https://raw.githubusercontent.com/jjoeldaniel/resume/main/img/dark-mode-button.png";
        for (let i = 0; i < buttons.length; i++) {
            buttons[i].style.color = "#000000"; 
        }
        console.log("dark mode: false");
    }
    // to dark
    else {
        dark = true;
        localStorage.setItem("dark_mode", "true");

        document.getElementById("dark-mode-button").src= "https://github.com/jjoeldaniel/resume/blob/main/img/sun.png?raw=true";
        for (let i = 0; i < buttons.length; i++) {
            buttons[i].style.color = "#FFFFFF"; 
        }
        console.log("dark mode: true");
    }
}