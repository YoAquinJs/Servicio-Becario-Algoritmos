document.addEventListener('DOMContentLoaded', function() {
    // Counter to keep track of the number of inputs created
    let inputCount = 0;

    // Add event listener to the button for adding new inputs
    document.getElementById('addInput').addEventListener('click', function() {
        // Increment inputCount for each new input
        inputCount++;

        // Create a container div for the new set of input fields
        const container = document.createElement('div');

        // Create custom label input for the set
        const customLabel = document.createElement('input');
        customLabel.type = 'text';
        customLabel.id = `customLabel${inputCount}`;
        customLabel.name = `customLabel${inputCount}`;
        customLabel.placeholder = 'Nombre del nodo';

        // Append custom label input to the container
        container.appendChild(customLabel);

        // Create new input elements for the set
        for (let i = 0; i < 2; i++) { // Change '3' to the desired number of input fields per set
            const input = document.createElement('input');
            input.type = 'text';


            switch (i) {
                case 0:
                    input.id = `Porcentaje Menor ${inputCount}-${i + 1}`;
                    input.name = `Porcentaje Menor ${inputCount}-${i + 1}`;
                    input.placeholder = 'Porcentaje Menor'
                    break;
                case 1:
                    input.id = `Porcentaje Mayor ${inputCount}-${i + 1}`;
                    input.name = `Porcentaje Mayor ${inputCount}-${i + 1}`;
                    input.placeholder = 'Porcentaje Mayor'
                    break;                
            }

            container.appendChild(input);
        }

        // Append the container to the inputContainer div
        document.getElementById('inputContainer').appendChild(container);
    });
});

