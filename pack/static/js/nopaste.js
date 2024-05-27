document.addEventListener('DOMContentLoaded', function() {
    var inputs = document.querySelectorAll('input[type="text"], input[type="password"]');
    inputs.forEach(function(input) {
        input.addEventListener('paste', function(event) {
            event.preventDefault();
        });
    });
});

window.addEventListener('contextmenu', function(event) {
    event.preventDefault();
});
