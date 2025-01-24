const startRecordingButton = document.getElementById('start-recording');
const fileInput = document.getElementById('file-input');
const audioPlayer = document.getElementById('audio-player');

let mediaRecorder;
let audioChunks = [];

// Function to start live recording
startRecordingButton.addEventListener('click', async () => {
    try {
        const stream = await navigator.mediaDevices.getUser Media({ audio: true });
        mediaRecorder = new MediaRecorder(stream);

        mediaRecorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };

        mediaRecorder.onstop = () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            const audioUrl = URL.createObjectURL(audioBlob);
            audioPlayer.src = audioUrl;
            audioChunks = []; // Reset for next recording
        };

        mediaRecorder.start();
        startRecordingButton.textContent = 'Stop Recording';
        startRecordingButton.onclick = () => {
            mediaRecorder.stop();
            startRecordingButton.textContent = 'Start Live Recording';
        };
    } catch (error) {
        console.error('Error accessing microphone:', error);
    }
});

// Function to handle file input
fileInput.addEventListener('change', event => {
    const file = event.target.files[0];
    if (file) {
        const audioUrl = URL.createObjectURL(file);
        audioPlayer.src = audioUrl;
    }
});