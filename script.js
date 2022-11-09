window.onload = init;

function init() {
    // document.getElementById('')
    document.getElementById("start-btn").addEventListener("click", scroll);
}

function scroll() {
    document.getElementById("section-label").scrollIntoView({ behavior: 'smooth', block: 'start'});
}