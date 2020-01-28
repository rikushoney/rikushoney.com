var window_y_position = window.pageYOffset;
var navbar = document.getElementById("navbar");
window.onscroll = function() {
    var current_y_position = window.pageYOffset;
    var delta_y = current_y_position - this.window_y_position;
    var navbar_height = this.navbar.getBoundingClientRect().height;
    if (delta_y < 0 || current_y_position < 4 * navbar_height) {
        this.navbar.style.top = "0";
    }
    else {
        var inverted_height = 0 - navbar_height;
        this.navbar.style.top = inverted_height.toString() + "px";
    }
    this.window_y_position = current_y_position;
}
