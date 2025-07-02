document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const submitBtn = document.getElementById("submitBtn");

    if (form && submitBtn) {
        form.addEventListener("submit", function (e) {
            e.preventDefault();
            submitBtn.disabled = true;
            submitBtn.innerText = "Carregando...";
            submitBtn.style.opacity = "0.7";

            setTimeout(() => {
                form.submit();
            }, 800);
        });
    }
});
