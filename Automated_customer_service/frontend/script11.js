function sendMessage() {
    const userInput = document.getElementById('user-input');
    const message = userInput.value;
    userInput.value = '';

    // Display the user's message
    displayMessage('You', message);

    // Send the message to the backend
    fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message }),
    })
    .then((response) => {
        if (!response.ok) {
            // Server returned a status code outside the 2xx range
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        // Display the response from the server
        displayMessage('AI agent', data.response);
    })
    .catch(error => {
        console.error('Fetch error:', error);
        displayMessage('AI agent', 'There was an error processing your request. Please try again later.');
    });
}

function displayMessage(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.className = sender === 'You' ? 'user-message' : 'bot-message';
    messageDiv.textContent = `${sender}: ${message}`;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}

