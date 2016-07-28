function request(url, finishedCallback) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4) {
            finishedCallback(xhttp);
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}