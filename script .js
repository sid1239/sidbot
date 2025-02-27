function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    let chatBox = document.getElementById("chat-box");
    let userMessage = `<p><strong>You:</strong> ${userInput}</p>`;
    chatBox.innerHTML += userMessage;

    document.getElementById("user-input").value = "";

    setTimeout(() => {
        let botResponse = getBotResponse(userInput);
        let botMessage = `<p><strong>SID BOT:</strong> ${botResponse}</p>`;
        chatBox.innerHTML += botMessage;
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 1000);
}

function getBotResponse(input) {
    let lowerInput = input.toLowerCase();
    if (lowerInput.includes("hello")) return "Hi there! How can I assist you? 😊";
    if (lowerInput.includes("how are you")) return "I'm just a bot, but I'm feeling great! 🚀";
    if (lowerInput.includes("bye")) return "Goodbye! Have a great day! 👋";
    return "I'm here to chat! What’s on your mind? 🤖";
}
