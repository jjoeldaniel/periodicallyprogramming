window.onload = init;
let dark = false;

function init() {

    // dark mode button listener
    document.getElementById("dark-mode-button").addEventListener("click", dark_mode);

    // default dark mode to false
    if (localStorage.getItem("dark_mode") === null) {
        localStorage.setItem("dark_mode", "false");
    }
    
    // grab stored dark mode setting
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
    }

    console.log("page ready");
}

// toggle dark mode
function dark_mode() {

    // to light
    if (dark) { 
        
        // set session setting and local storage
        dark = false;
        localStorage.setItem("dark_mode", "false");

        // switch button icon
        document.getElementById("dark-mode-button").src= "https://raw.githubusercontent.com/jjoeldaniel/resume/main/img/dark-mode-button.png";

        // change background colors
        document.body.style.backgroundColor= "#f5f5f5";
        document.body.style.color= "#343434";

        console.log("dark mode: false");
    }
    // to dark
    else {

        // set session setting and local storage
        dark = true;
        localStorage.setItem("dark_mode", "true");

        // switch button icon
        document.getElementById("dark-mode-button").src= "https://github.com/jjoeldaniel/resume/blob/main/img/sun.png?raw=true";

        // change background colors
        document.body.style.backgroundColor= "#343434";
        document.body.style.color= "#f5f5f5";

        console.log("dark mode: true");
    }
}