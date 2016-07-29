/*
* This is the circle Class
*/

function Circle(id) {
    this.id = id;
    this.element = document.getElementById(id);
    
    this.element.className += " circle";
    var that = this;
    setTimeout(function() {
        that.element.className += " slow";
    }, 10);
}

Circle.prototype.setColor = function(color) {
    this.element.style.backgroundColor = color;
}

Circle.prototype.getColor = function() {
    return this.element.style.backgroundColor;
}

Circle.prototype.no = function() {
    var circle = this;
    setTimeout(function() {
            circle.setColor("#ff0000");
    }, 200);
    setTimeout(function() {
        circle.element.className += " shake";
        setTimeout(function() {
            circle.element.className = circle.element.className.replace(" shake", "");
        }, 1000);
    }, 400);
}

Circle.prototype.yes = function() {
    this.setColor("#00ff00")
}
