let help;
let running = false;

function startCounter() {
    if (!running) {
        running = true;
        help = setInterval(() => {
            document.getElementsByClassName('count')[0].innerHTML = Number(document.getElementsByClassName('count')[0].innerHTML) + 1;
        }, 1000);
    }
}

function stopCounter() {
    clearInterval(help);
    running = false;
}

function clearCounter() {
    document.getElementsByClassName('count')[0].innerHTML = 0;
}