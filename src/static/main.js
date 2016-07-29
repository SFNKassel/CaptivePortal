/*
* This is the main file of the JS foo
*/

var circle;

//first do some init stuff
function onReady() {
    circle = new Circle("circle");
    
    readState(function(name) {
        if(name != false) {
            displayLogout(name);
        } else {
            var user = document.URL.split("?user=")[1];
            if(user) {
                document.getElementById("username").value = user;
                document.getElementById("password").focus();
            }
            displayLogin();
        }
    });
}

//now the comunication functions
function login() {
    var user = document.getElementById("username").value;
    var passwd = document.getElementById("password").value;
    
    request("/api/login?user=" + user + "&passwd=" + passwd, function(xhttp) {
        if(xhttp.status == 202) {
            //authentication sucessfully
            hide("login");
            setTimeout(function() {
                circle.yes();
            }, 100);
            var name = xhttp.responseText;
            setTimeout(function() {
                window.location.reload();
            }, 1000);
            setTimeout(function() {
                displayLogout(name);
            }, 2000);
        } else {
            //next try :(
            circle.no();
            newTry();
        }
    });
  return false; //for not reloading the page
}

function logout() {
  request("/api/logout", function(xhttp) {
      //nothing to do here
      displayLogin();
  });
  return false; //for not reloading the page
}


function readState(callback) {
    request("/api/state", function(xhttp) {
        if(xhttp.status == 200) {
            var name = xhttp.responseText;
            callback(name);
        } else {
            callback(false);
        }
    });
}

//and finally the style modifying functions
function displayLogin() {
    hide("logout");
    display("login");
    circle.setColor("rgb(212, 29, 140)");
    
    setTimeout(function(){
        document.getElementById("username").focus();
    }, 1100);
}

function newTry() {
    document.getElementById("password").value = "";
    document.getElementById("password").focus();
}

function displayLogout(name) {
    name = JSON.parse(name);
    document.getElementById("name").innerHTML = name.name;
    circle.setColor(stringToColor(name.user));
    
    hide("login");
    display("logout");
    setTimeout(function(){
        document.getElementById("logout_button").focus();
    }, 1100);
}
