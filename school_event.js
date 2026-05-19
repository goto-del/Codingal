// Simulated raw data representing a school event from a database
const rawEventData = {
    id: "EVT-2026-001",
    name: "Annual Science Fair",
    date: "2026-10-15",
    time: "09:00 AM - 03:00 PM",
    location: "Main School Auditorium",
    organizer: "Science Department",
    participantsExpected: 250,
    highlights: [
        "Robotics Exhibition",
        "Chemistry Magic Show",
        "Guest Speaker: Dr. Smith"
    ]
};

// DOM Elements
const loadBtn = document.getElementById('load-btn');
const loadingMessage = document.getElementById('loading-message');
const dataContainer = document.getElementById('data-container');
const jsonTextDisplay = document.getElementById('json-text-display');
const eventDetailsDisplay = document.getElementById('event-details');

function loadData() {
    // 1. Initial State: Show loading message and hide data container
    loadBtn.disabled = true;
    loadBtn.textContent = "Fetching...";
    loadingMessage.classList.remove('hidden');
    dataContainer.classList.add('hidden');
    
    // Simulate server latency using setTimeout (2 seconds)
    setTimeout(() => {
        // 2. Convert event data to JSON text (Serialization)
        const jsonText = JSON.stringify(rawEventData, null, 4); // 4 spaces for readable formatting
        
        // 3. Parse it back into a JavaScript object (Deserialization)
        // In a real application, 'jsonText' is what you would receive from the server via fetch/XHR.
        const parsedEventData = JSON.parse(jsonText);
        
        // 4. Show the final event details on the webpage
        
        // Display the JSON Text
        jsonTextDisplay.textContent = jsonText;
        
        // Display the Parsed Object properties dynamically
        eventDetailsDisplay.innerHTML = `
            <p><strong>Event Name:</strong> ${parsedEventData.name}</p>
            <p><strong>Date:</strong> ${parsedEventData.date}</p>
            <p><strong>Time:</strong> ${parsedEventData.time}</p>
            <p><strong>Location:</strong> ${parsedEventData.location}</p>
            <p><strong>Organizer:</strong> ${parsedEventData.organizer}</p>
            <p><strong>Expected Participants:</strong> ${parsedEventData.participantsExpected}</p>
            <p><strong>Highlights:</strong></p>
            <ul>
                ${parsedEventData.highlights.map(highlight => `<li>${highlight}</li>`).join('')}
            </ul>
        `;
        
        // Update UI State: Hide loading message, show the data container
        loadingMessage.classList.add('hidden');
        dataContainer.classList.remove('hidden');
        
        loadBtn.textContent = "Data Loaded Successfully!";
        
        // Optional: Reset button after a few seconds to allow reloading
        setTimeout(() => {
            loadBtn.disabled = false;
            loadBtn.textContent = "Fetch Event Data Again";
        }, 3000);
        
    }, 2000); // 2000 milliseconds = 2 seconds loading simulation
}
