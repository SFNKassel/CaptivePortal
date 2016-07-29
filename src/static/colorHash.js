function stringToColor(str) {
    return "#" + CryptoJS.MD5(str).toString().substr(0,6);
}

function updateCircle() {
    circle.setColor(stringToColor(document.getElementById("username").value))
}
