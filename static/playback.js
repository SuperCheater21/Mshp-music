function playSong(songUrl) {
    // Create an AudioContext
    alert("boba")
    const audioCtx = new AudioContext();

    // Create an Audio element (hidden)
    const audioElement = document.createElement('audio');
    audioElement.src = songUrl;
    audioElement.style.display = 'none';
    document.body.appendChild(audioElement);

    // Create a source node from the audio element
    const sourceNode = audioCtx.createMediaElementSource(audioElement);

    // Create a gain node to control volume (optional)
    const gainNode = audioCtx.createGain();

    // Connect source to gain (optional) and then to destination
    sourceNode.connect(gainNode);
    gainNode.connect(audioCtx.destination);

    // Play the audio
    audioElement.play();

    // Handle errors (optional)
    audioElement.onerror = function(error) {
        console.error('Error playing song:', error);
    };
}

// Get the song URL from the template context
const songUrl = '{{ song.file.url }}';  // Replace with your template variable name

// Call the playSong function with the URL
playSong(songUrl);