import * as backend from "./backend_connection.js"
import { onLoadFile } from "./file_uploader.js"

onLoadFile.addEventListener("onLoadFile", event => {
    backend.sendConfigFile("TYPE", event.detail.fileContent);
})

document.addEventListener('DOMContentLoaded', function() {
    // Counter to keep track of the number of inputs created
    let inputCount = 0;
    
    // Add event listener to the button for adding new inputs
    document.getElementById('add-input').addEventListener('click', function() {
        // Increment inputCount for each new input
    inputCount++;
    
        // Get the name of the label from labelSet
        const labelSetName = document.getElementById('label-set').value;
    
        // Create a container div for the new set of input fields
        const container = document.createElement('div');
    
        // Create label from input labelSet
        const label = document.createElement('label');
        label.textContent = `${labelSetName}`
    
        // Append label input to the container
        container.appendChild(label);
    
        // Create new input elements for the set
        for (let i = 0; i < 2; i++) { // Change '3' to the desired number of input fields per set
            const input = document.createElement('input');
            input.type = 'text';
    
            switch (i) {
                case 0:
                    input.id = `Peso_Menor_${inputCount}_${i + 1}`;
                    input.name = `Peso Menor ${inputCount}-${i + 1}`;
                    input.placeholder = 'Peso Menor'
                    break;
                case 1:
                    input.id = `Peso_Mayor_${inputCount}_${i + 1}`;
                    input.name = `Peso Mayor ${inputCount}-${i + 1}`;
                    input.placeholder = 'Peso Mayor'
                    break;
            }

            container.appendChild(input);
        }

        // Append the container to the inputContainer div
        document.getElementById('input-container').appendChild(container);
    });

// Add event listener to the send button
    document.getElementById('send').addEventListener('click', function() {
        // Construct JSON object with the data to send
        const formData = [];

        // Get labels text content
        const labels = document.querySelectorAll('#input-container label');
        labels.forEach(label => {
            formData.push(label.textContent);
        });

        // Log JSON data before sending
        console.log('String data nodos: ', formData );

        // Send the string to the backend (replace 'your-backend-url' with your actual backend URL)
        fetch('your-backend-url', {
            method: 'POST',
            headers: {
                'Content-Type': 'text/plain' // Specify the content type as plain text
            },
            body: formData // Send the string as the request body
        })
    .then(response => {
        // Handle the response from the backend
        if (response.ok) {
            console.log('Data sent successfully');
        } else {
            console.error('Failed to send data to the backend');
        }
    })
    .catch(error => {
    console.error('Error:', error);
    }); 
});

    document.getElementById('send').addEventListener('click', function() {
        // Construct JSON object with the data to send
        const weightValues = []

        // Get labels text content
        const weights = document.querySelectorAll('#input-container input');
        weights.forEach(function(input) {
            if(input.id != 'label-set'){
                console.log(input.value)
                weightValues.push(input.value);
            }
        });

        const weightString = weightValues.join(', ')

        // Log JSON data before sending
        console.log('String data pesos: ', weightString);

        // Send the string to the backend (replace 'your-backend-url' with your actual backend URL)
        fetch('your-backend-url', {
            method: 'POST',
            headers: {
                'Content-Type': 'text/plain' // Specify the content type as plain text
            },
            body: weightString // Send the string as the request body
        })
        .then(response => {
            // Handle the response from the backend
            if (response.ok) {
                console.log('Data sent successfully');
            } else {
                console.error('Failed to send data to the backend');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        }); 

    });

    // Add event listener to the button for sending parameters
    document.getElementById('send-add-parameters').addEventListener('click', function() {
        // Get the input fields within the "parametros-adicionales" div
        const parametrosAdicionalesInputs = document.querySelectorAll('.additional-parameters input');

        // Create an array to store the values of the input fields
        const parametrosAdicionalesValues = [];

        // Loop through each input field to retrieve its value
        parametrosAdicionalesInputs.forEach(function(input) {
            console.log('Input value: ', input.value);
            parametrosAdicionalesValues.push(input.value);
        });

        // Concatenate the values into a single string
        const parametrosAdicionalesString = parametrosAdicionalesValues.join(', ');

        console.log('Parámetros adicionales: ', parametrosAdicionalesString);

        // Send the string to the backend (replace 'your-backend-url' with your actual backend URL)
        fetch('your-backend-url', {
            method: 'POST',
            headers: {
                'Content-Type': 'text/plain' // Specify the content type as plain text
            },
            body: parametrosAdicionalesString // Send the string as the request body
        })
        .then(response => {
            // Handle the response from the backend
            if (response.ok) {
                console.log('Data sent successfully');
            } else {
                console.error('Failed to send data to the backend');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        }); 
    });


    // Function that gets the .txt file from the server to load it to display it to the frontend
    function displayTextFile(filename) {
        const xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    document.getElementsByClassName('backend-text').textContent = xhr.responseText;
                } else {
                    console.error('Failed to load the file:', xhr.status);
                }
            }
        };
        // Update the URL to point to the backend endpoint
        xhr.open('GET', 'http://your-backend-url/' + filename, true);
        xhr.send();
    }
    
    // Call the function to load and display the text file from the backend
    displayTextFile('criteria-parameters.txt');
});
