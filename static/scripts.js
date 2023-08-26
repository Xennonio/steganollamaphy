// Get the input element and the character count element
const msgInput = document.getElementById('msg');
const charCount = document.getElementById('charCount');

// Set the maximum character limit
const maxCharacters = 1000;

// Add an event listener to the input field to track changes
msgInput.addEventListener('input', function() {
    // Get the current text length
    const currentLength = this.value.length;

    // Update the character count element
    charCount.textContent = currentLength + '/' + maxCharacters;
});