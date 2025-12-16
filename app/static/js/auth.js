document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("loginForm");
    const alertBox = document.getElementById("loginAlert");

    if (loginForm) {
        loginForm.addEventListener("submit", async function (e) {
            e.preventDefault();
            alertBox.classList.add("d-none");
            alertBox.innerText = "";

            const formData = new FormData(loginForm);

            try {
                const response = await fetch("/auth/login", {
                    method: "POST",
                    body: formData
                });

                if (response.ok) {
                    // Login success -> redirect
                    window.location.href = "/dashboard";
                } else {
                    // Login failed
                    const errorData = await response.json(); // Try to parse JSON error
                    alertBox.innerText = errorData.detail || "Invalid credentials";
                    alertBox.classList.remove("d-none");
                }
            } catch (error) {
                console.error("Login Error:", error);
                alertBox.innerText = "Something went wrong. Please try again.";
                alertBox.classList.remove("d-none");
            }
        });
    }
});
