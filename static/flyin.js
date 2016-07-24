function display(id) {
    document.getElementById(id).className += " flyin_visible";
    setTimeout(function() {
        document.getElementById(id).className += " flyin_active";
    }, 10);
}

function hide(id) {
    var element = document.getElementById(id);
    element.className = element.className.replace(" flyin_active", "")
    element.className = element.className.replace(" flyin_visible", "")
}