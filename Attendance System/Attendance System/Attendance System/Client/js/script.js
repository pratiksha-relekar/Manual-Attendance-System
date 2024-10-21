function validateLogin() {
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    let hasLowercase = /[a-z]/.test(password);
    let hasUppercase = /[A-Z]/.test(password);
    let hasNumber = /\d/.test(password);

    if (email === "" || password === "") {
        alert("Please fill all fields.");
        return false;
    }

    if (!emailPattern.test(email)) {
        alert("Please enter a valid email address.");
        return false;
    }

    if (!(hasLowercase && hasUppercase && hasNumber)) {
        alert("Password must contain at least one lowercase letter, one uppercase letter, and one number.");
        return false;
    }

    return true;
}
