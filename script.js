document.addEventListener("DOMContentLoaded", function() {
    const gridContainer = document.getElementById("gridContainer");

    // Create 16 buttons
    for (let i = 1; i <= 4; i++) {
        const button = document.createElement("button");
        button.classList.add("button");
        button.textContent = "Button " + i;
        gridContainer.appendChild(button);
    }
});