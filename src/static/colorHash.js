function stringToColor(str) {
    return "#" + CryptoJS.MD5(str).toString().substr(0,6);
}

function updateCircle() {
    document.getElementById('circle').style.backgroundColor =  stringToColor(document.getElementById("username").value)
}