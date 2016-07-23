function onReady() {
    document.getElementById('username').focus();
}

var firstrun = true;
function error() {
    setTimeout(function() {
            document.getElementById("circle").style.backgroundColor = "#ff0000";
    }, 100);
    setTimeout(function() {
        document.getElementById("circle").className = " shake";
        setTimeout(function() {
            document.getElementById("circle").className = "";
        }, 500);
    }, 400);
    document.getElementById("password").value = "";
    document.getElementById("password").focus();
}

function ok(name) {
    var before = document.getElementById("circle").style.backgroundColor;
    document.getElementById("circle").style.backgroundColor = "#00ff00";
    document.getElementById("login").style.display = "none";
    document.getElementById("name").innerHTML = name;
    document.getElementById("logout").style.display = "block";
    
    setTimeout(function() {
        document.getElementById("logout").style.top = "0px";
    }, 1000);
    
    setTimeout(function() {
        document.getElementById("circle").style.backgroundColor = before;
    }, 2000);
}

function login() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4) {
        if(xhttp.status == 202) {
            ok(xhttp.responseText);
            //user authenticated
        } else if(xhttp.status == 200) {
            //user already authenticated
        } else {
            //user have to be authenticated
            error();
        }
    }
  };
  xhttp.open("GET", "api/login?user=" + document.getElementById("username").value + "&passwd=" + document.getElementById("password").value, true);
  xhttp.send();
  return false; //for not reloading the page
}

function logout() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4) {
        if(xhttp.status == 202) {
            ok(xhttp.responseText);
            //user authenticated
        } else if(xhttp.status == 200) {
            //user already authenticated
        } else {
            //user have to be authenticated
            error();
        }
    }
  };
  xhttp.open("GET", "api/logout", true);
  xhttp.send();
  return false; //for not reloading the page
}
