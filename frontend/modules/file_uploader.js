export let uploadedFileContent;

export function handleFileSelect(event) {
    const file = event.target.files[0];

    if (!file)
        return;

    const reader = new FileReader();
    reader.onload = function(event) {
        uploadedFileContent = event.target.result;
    };
    reader.readAsText(file);
}
