document.addEventListener('DOMContentLoaded', function(){
    // Get buttons and input fields
    const logInButton = document.getElementById('send-login')
    const signUpButton = document.getElementById('create-session')
    const logInUsername = document.getElementById('login-usname')
    const signUpUsername = document.getElementById('signup-usname')

    // Function to redirect to page
    function handleRedirection(username, page){ 
        if (username && username.trim() != ""){
            // Redirects to app.html
            window.location.href = page + '?username=' + encodeURIComponent(username);
        } else {
            alert('Por favor, ingrese un nombre de usuario.');
        }
    }

    logInButton.addEventListener('click', function(){
        handleRedirection(logInUsername.value, 'app.html');
    });

    signUpButton.addEventListener('click', function(){
        handleRedirection(signUpUsername.value, 'app.html');
    });
});