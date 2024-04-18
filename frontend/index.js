import * as backend from "./modules/backend_connection.js"
import { uploadedFileContent, handleFileSelect } from "./modules/file_uploader.js"
import { getParsedMatrix } from "./modules/matrix_parser.js"
import { downloadDataAsFile } from "./modules/downloader.js"

function visualizeRequestOutput(request, htmlElem, onSuccesMsg, onErrorMsg){
    const prevText = htmlElem.innerHTML;
    htmlElem.innerHTML = "...";
    request.then(_ => {
        htmlElem.innerHTML = onSuccesMsg;
        setTimeout(_ => {
            htmlElem.innerHTML = prevText;
        }, 800);
    }).catch(err => {
        htmlElem.innerHTML = onErrorMsg;
        setTimeout(_ => {
            htmlElem.innerHTML = prevText;
        }, 1500);
    });
}

const configTypeDropdownId = "config-type";
const textUplaodId = "text-upload";
const fileUploadId = "file-upload";
const sendTextButtonId = "send-text-button";
const sendFileButtonId = "send-file-button";
const getConfigButtonId = "get-config-button";
const executeButtonId = "execute-button";
const matrixTypeId = "matrix-type";
const getMatrixButtonId = "matrix-button";
const matrixDisplayId = "matrix-display";

document.addEventListener("DOMContentLoaded", _ => {
    const configTypeDropdown = document.getElementById(configTypeDropdownId);

    const textConfigInput = document.getElementById(textUplaodId);
    const fileConfigInput = document.getElementById(fileUploadId);
    fileConfigInput.addEventListener("change", handleFileSelect);

    const sendTextButton = document.getElementById(sendTextButtonId);
    sendTextButton.addEventListener("click", _ => {
        const request = backend.sendConfigFile(configTypeDropdown.value, textConfigInput.value);
        visualizeRequestOutput(request, sendTextButton, "Enviado", "Fallido");
    });
    const sendFileButton = document.getElementById(sendFileButtonId);
    sendFileButton.addEventListener("click", _ => {
        const request = backend.sendConfigFile(configTypeDropdown.value, uploadedFileContent);
        visualizeRequestOutput(request, sendFileButton, "Enviado", "Fallido");
    });

    const getConfigButton = document.getElementById(getConfigButtonId);
    getConfigButton.addEventListener("click", _ => {
        const request = backend.getConfigFile(configTypeDropdown.value);
        request.then(config => {
            downloadDataAsFile(config, configTypeDropdown.value);
        });
        visualizeRequestOutput(request, getConfigButton, "Obtenido", "Fallido");
    });

    const executeButton = document.getElementById(executeButtonId);
    executeButton.addEventListener("click", _ => {
        const request = backend.execute();
        request.then(response => {
            console.log(response);
        });
        visualizeRequestOutput(request, executeButton, "Ejecutado", "Fallido");
    });

    const matrixTypeInput = document.getElementById(matrixTypeId);
    const getMatrixButton = document.getElementById(getMatrixButtonId);
    const matrixDisplay = document.getElementById(matrixDisplayId);
    getMatrixButton.addEventListener("click", _ => {
        const request = backend.getMatrix(matrixTypeInput.value);
        request.then(matrix => {
            const parsedMatrix = getParsedMatrix(matrix);

            matrixDisplay.innerText = parsedMatrix;
            downloadDataAsFile(parsedMatrix, matrixTypeInput.value + "-matrix");
        });
        visualizeRequestOutput(request, getMatrixButton, "Obtenido", "Fallido");
    });
});
