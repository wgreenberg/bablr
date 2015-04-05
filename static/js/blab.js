function ready() {
    var form = document.querySelector('#userInput');
    console.log('wat');
    form.onsubmit = blab;
}

function blab() {
    var userInput = document.querySelector('#userText').value;
    var phraseBox = document.querySelector('#phrase');
    var req = new XMLHttpRequest();
    req.onreadystatechange = function () {
        if (req.readyState === 4) {
            var res = JSON.parse(req.responseText);
            phrase.innerText = res.message;
        }
    }
    req.open('GET', 'blab?input=' + encodeURIComponent(userInput), true);
    req.send();
    return false;
}
