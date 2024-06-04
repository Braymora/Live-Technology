const iconEyes = document.querySelector(".showHidePw");
const input = document.getElementById("input");

iconEyes.addEventListener("click", function () {
    if (input.type === "password") {
        input.type = "text";
        iconEyes.classList.add("hidden");
    } else {
        input.type = "password";
        iconEyes.classList.remove("hidden");
    }
});
