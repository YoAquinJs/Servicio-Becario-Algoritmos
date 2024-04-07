document.addEventListener('DOMContentLoaded', function() {
    // Counter to keep track of the number of inputs created
    let inputCount = 0;
    
    // Add event listener to the button for adding new inputs
    document.getElementById('addInput').addEventListener('click', function() {
        // Increment inputCount for each new input
    inputCount++;
    
        // Get the name of the label from labelSet
        const labelSetName = document.getElementById('labelSet').value;
    
        // Create a container div for the new set of input fields
        const container = document.createElement('div');
    
        // Create label from input labelSet
        const label = document.createElement('label');
        label.textContent = `${labelSetName}`
    
        // Append label input to the container
        container.appendChild(label);
    
        // Create new input elements for the set
        for (let i = 0; i < 4; i++) { // Change '3' to the desired number of input fields per set
            const input = document.createElement('input');
            input.type = 'text';
    
            switch (i) {
                case 0:
                    input.id = `Porcentaje_Menor_${inputCount}_${i + 1}`;
                    input.name = `Porcentaje Menor ${inputCount}-${i + 1}`;
                    input.placeholder = 'Porcentaje Menor'
                    break;
                case 1:
                    input.id = `Porcentaje_Mayor_${inputCount}_${i + 1}`;
                    input.name = `Porcentaje Mayor ${inputCount}-${i + 1}`;
                    input.placeholder = 'Porcentaje Mayor'
                    break;
                default:
                    input.id = `Proyecto_${inputCount}_${i - 1}`;
                    input.name = `Proyecto ${inputCount}-${i - 1}`;
                    input.placeholder = `Proyecto ${inputCount}-${i - 1}`;              
            }

            container.appendChild(input);
        }

        // Append the container to the inputContainer div
        document.getElementById('inputContainer').appendChild(container);
    });

// Add event listener to the send button
    document.getElementById('send').addEventListener('click', function() {
        // Construct JSON object with the data to send
        const formData = [];

        // Get labels text content
        const labels = document.querySelectorAll('#inputContainer label');
        labels.forEach(label => {
            // Ignore label containing "Parámetros adicionales"
            if (label.textContent.trim() !== 'Parámetros adicionales') {
                formData.push(label.textContent);
            }
        });

        // Log JSON data before sending
        console.log('JSON data:', JSON.stringify(formData));
/*
        // Convert JSON object to string
        const jsonData = JSON.stringify(formData);

        // Send JSON data to backend server
        fetch('YOUR_BACKEND_ENDPOINT', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: jsonData
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Network response was not ok.');
        })
        .then(data => {
            console.log('Response from server:', data);
        })
        .catch(error => {
            console.error('Error sending data to server:', error);
        }); */
    });
});
