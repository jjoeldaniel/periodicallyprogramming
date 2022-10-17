// Dark Mode is off by default
let dark = false;

if (localStorage.getItem("dark_mode") === null) {
    localStorage.set("dark_mode", "false");
}

if (localStorage.getItem("dark_mode") === "true") {
    dark = true;
}
else if (localStorage.getItem("dark_mode") === "false") {
    dark = false;
}


// Toggle Dark Mode
function dark_mode() {
    document.body.classList.toggle("projects-dark-mode")
    let buttons = document.getElementsByClassName("btn");
    dark = !dark;

    if (dark) {
        document.getElementById("toggle").src= "https://github.com/jjoeldaniel/resume/blob/main/img/sun.png?raw=true";
        localStorage.set("dark_mode", "false");

        for (let i = 0; i < buttons.length; i++) {
            buttons[i].style.color = "#000000"; 
        }
    }
    else {
        document.getElementById("toggle").src= "https://raw.githubusercontent.com/jjoeldaniel/resume/main/img/dark-mode-button.png";
        localStorage.set("dark_mode", "true");

        for (let i = 0; i < buttons.length; i++) {
            buttons[i].style.color = "#FFFFFF"; 
        }
    }
}