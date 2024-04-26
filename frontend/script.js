// Define an object mapping algorithm options to background colors
const algorithmColors = {
    'Calculate Credibility Matrix': '#8495b9',
    'Calculate Sorting': '#c9b14a',
    'Project Level': '#66cc99',
    'Portfolio Level': '#aa6fd1'
};

// .bg-credibility { background-color: #8495b9; }
// .bg-sorting { background-color: #c9b14a; }
// .bg-project { background-color: #66cc99; }
// .bg-portfolio { background-color: #aa6fd1; }

// Function to set the background color based on the selected value
function setBackgroundColor(selectedValue) {
    // Get the container element
    var container = document.getElementById('container');
    var buttons = document.getElementsByClassName('hover-bg');
    
    // Set the background color based on the selected value
    var color = algorithmColors[selectedValue] || '#8495b9';
    container.style.backgroundColor = color;
    
    // Apply the color only when the button is hovered over
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('mouseover', function() {
            this.style.backgroundColor = color;
        });
        buttons[i].addEventListener('mouseout', function() {
            this.style.backgroundColor = ''; // Reset to default when not hovered
        });
    }
}

// Add event listener when the DOM content is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Call the function to set the background color when the page loads
    var selectedValue = document.getElementById('algorithm-type').value;
    setBackgroundColor(selectedValue);

    // Add event listener to the select element
    document.getElementById('algorithm-type').addEventListener('change', function() {
        // Get the selected value
        var selectedValue = this.value;

        // Update the text of the h2 element based on the selected value
        document.getElementById('algo-title').textContent = selectedValue;

        // Call the function to set the background color based on the selected value
        setBackgroundColor(selectedValue);
    });
});
