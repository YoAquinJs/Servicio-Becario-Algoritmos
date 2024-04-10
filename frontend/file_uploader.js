export const onLoadFile = new EventTarget();

function handleFileSelect(event) {
    const file = event.target.files[0];

    if (!file)
        return;

    const reader = new FileReader();
    reader.onload = function(event) {
        const fileContent = event.target.result;
        onLoadFile.dispatchEvent(new CustomEvent('onLoadFile', {
            detail: {
                fileContent: fileContent
            }
        }));
    };
    reader.readAsText(file);
}

const fileUploadId = "file-upload"
const fileInput = document.getElementById(fileUploadId);
fileInput.addEventListener('change', handleFileSelect);
