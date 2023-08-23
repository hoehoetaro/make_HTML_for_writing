function copyToClipboard(elementId) {
    var aux = document.createElement("textarea");
    aux.innerHTML = document.getElementById(elementId).textContent;
    document.body.appendChild(aux);
    aux.select();
    document.execCommand("copy");
    document.body.removeChild(aux);
}