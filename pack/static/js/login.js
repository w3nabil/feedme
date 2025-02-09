document.addEventListener("DOMContentLoaded", function () {
    const inputs = document.querySelectorAll("input");

    inputs.forEach(input => {
        input.addEventListener("focus", () => {
            input.style.background = "rgba(255, 255, 255, 0.3)";
        });
        input.addEventListener("blur", () => {
            input.style.background = "rgba(255, 255, 255, 0.2)";
        });
    });
});
