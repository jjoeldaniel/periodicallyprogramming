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

    // Hide dropdown for mobile
    if (window.matchMedia("(max-width: 749px)").matches) {
        console.log("mobile");
        const element = document.getElementById('dropbtn');
        element.style.display = 'none';
    }
    else console.log("not mobile");

    // initialize dark mode
    if (dark) {
        document.body.classList.toggle("projects-dark-mode")
        document.getElementById("dark-mode-button").src= "https://github.com/jjoeldaniel/resume/blob/main/img/sun.png?raw=true";
    }

    console.log("page ready");
}

// Toggle Dark Mode
function dark_mode() {
    let element = document.getElementById('projects');

    // to light
    if (dark) { 
        dark = false;
        localStorage.setItem("dark_mode", "false");
        document.getElementById("dark-mode-button").src= "https://raw.githubusercontent.com/jjoeldaniel/resume/main/img/dark-mode-button.png";

        document.body.style.backgroundColor= "#f5f5f5";
        document.body.style.color= "#343434";

        console.log("dark mode: false");
    }
    // to dark
    else {
        dark = true;
        localStorage.setItem("dark_mode", "true");
        document.getElementById("dark-mode-button").src= "https://github.com/jjoeldaniel/resume/blob/main/img/sun.png?raw=true";

        document.body.style.backgroundColor= "#343434";
        document.body.style.color= "#f5f5f5";

        console.log("dark mode: true");
    }
}