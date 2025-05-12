// Function to get the current time in HH:MM format
function getTimestamp() {
    const now = new Date();
    return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

async function sendMessage() {
    const inputBox = document.getElementById("userInput");
    const chatbox = document.getElementById("chatbox");
    const userInput = inputBox.value.trim();

    if (!userInput) return;

    // Display user message with timestamp
    const userMessage = document.createElement("p");
    userMessage.innerHTML = `<b>You [${getTimestamp()}]:</b> ${userInput}`;
    chatbox.appendChild(userMessage);
    inputBox.value = "";

    // Auto-scroll
    chatbox.scrollTop = chatbox.scrollHeight;

    // Display loading message
    const loadingMessage = document.createElement("p");
    loadingMessage.innerHTML = `<i>Loading...</i>`;
    chatbox.appendChild(loadingMessage);
    chatbox.scrollTop = chatbox.scrollHeight;

    try {
        // Send to backend
        const BACKEND_URL = "https://your-backend-url.com/chat"; // update after deploying
        const response = await fetch(BACKEND_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ user_input: userInput })
        });

        const data = await response.json();

        // Remove loading message
        loadingMessage.remove();

        // Create AI message element
        const aiMessage = document.createElement("p");
        aiMessage.innerHTML = `<b>CodeLogic [${getTimestamp()}]:</b> <span></span>`;
        const span = aiMessage.querySelector("span");
        chatbox.appendChild(aiMessage);
        chatbox.scrollTop = chatbox.scrollHeight;

        // Type the AI response with animation
        await typeText(span, data.response);

    } catch (error) {
        // Remove loading and show error
        loadingMessage.remove();
        const errorMessage = document.createElement("p");
        errorMessage.innerHTML = `<b>CodeLogic [${getTimestamp()}]:</b> Sorry, something went wrong. Please try again.`;
        chatbox.appendChild(errorMessage);
        chatbox.scrollTop = chatbox.scrollHeight;
    }
}

// Typing effect function
async function typeText(element, text) {
    for (let i = 0; i < text.length; i++) {
        element.textContent += text.charAt(i);
        await new Promise(resolve => setTimeout(resolve, 15));
        element.parentElement.parentElement.scrollTop = element.parentElement.parentElement.scrollHeight;
    }
}

// ENTER key support
document.getElementById("userInput").addEventListener("keydown", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});