document.getElementById("form").addEventListener('submit', async function(e) {
    e.preventDefault();  // Prevent default form submission
    
    // Get form elements
    const form = e.target;
    const submitButton = form.querySelector('button[type="submit"]');
    const messageDiv = document.getElementById('message');
    
    // Show loading state
    submitButton.disabled = true;
    submitButton.textContent = 'Authenticating...';
    messageDiv.textContent = '';
    messageDiv.className = 'message';
    
    // Prepare form data
    const formData = {
        username: form.first.value,
        password: form.pass.value

    };

    //const url = 'http://127.0.0.1:8000/token'
    //const url = 'https://radrs.icraf.org/respi/user/login'
    //const url = 'https://cors-anywhere.herokuapp.com/https://radrs.icraf.org/respi/user/login'
    const url = '/token'

    try {
        // Send AJAX request using the fetch api
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                "Accept" : "application/json",
                //'Content-Type': 'application/json; charset=UTF-8'
                'Content-Type' : 'application/x-www-form-urlencoded'
            },
            //body: JSON.stringify(formData)
            body: new URLSearchParams({
                grant_type: "password",
                username: formData.username,
                password: formData.password,
                scope: "",
                client_id: "string",
                client_secret: "string"
            })
        });

        const data = await response.json();

        console.log('Response data:', data);
        
        if (response.ok) {
            // Login successful
            messageDiv.textContent = 'Login successful! Redirecting...';
            messageDiv.className = 'message success';
            
            // Redirect to dashboard after delay
            setTimeout(() => {
                window.location.href = '/index.html';
            }, 1500);
        } else {
            // Login failed
            throw new Error(data.message || 'Incorrect Name or Password!');
        }
    } catch (error) {
        // Handle errors
        messageDiv.textContent = error.message || 'An error occurred. Please try again.';
        messageDiv.className = 'message error';
        console.error('Login error:', error)
    } finally {
        // Reset button state
        submitButton.disabled = false;
        submitButton.textContent = 'Access Dashboard';
    }
});