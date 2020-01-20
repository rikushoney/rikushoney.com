var window_y_position = window.pageYOffset;
var navbar = document.getElementById("navbar");
window.onscroll = function() {
    var current_y_position = window.pageYOffset;
    if (this.window_y_position < current_y_position) {
        this.navbar.style.top = "0";
    }
    else {
        this.navbar.style.top = (0 - this.navbar.getBoundingClientRect().height).toString();
    }
    this.window_y_position = current_y_position;
}
