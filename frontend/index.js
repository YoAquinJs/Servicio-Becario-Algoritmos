import * as backend from "./modules/backend_connection.js"
import { uploadedFileContent, handleFileSelect } from "./modules/file_uploader.js"
import { getParsedMatrix } from "./modules/matrix_parser.js"
import { downloadDataAsFile } from "./modules/downloader.js"

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
        backend.sendConfigFile(configTypeDropdown.value, textConfigInput.value);
    });
    const sendFileButton = document.getElementById(sendFileButtonId);
    sendFileButton.addEventListener("click", _ => {
        backend.sendConfigFile(configTypeDropdown.value, uploadedFileContent);
    });

    const getConfigButton = document.getElementById(getConfigButtonId);
    getConfigButton.addEventListener("click", _ => {
        backend.getConfigFile(configTypeDropdown.value).then(config => {
            downloadDataAsFile(config, configTypeDropdown.value);
        });
    });

    const executeButton = document.getElementById(executeButtonId);
    executeButton.addEventListener("click", _ => {
        backend.execute().then(response => {
            console.log(response);
        });
    });

    const matrixTypeInput = document.getElementById(matrixTypeId);
    const getMatrixButton = document.getElementById(getMatrixButtonId);
    const matrixDisplay = document.getElementById(matrixDisplayId);
    getMatrixButton.addEventListener("click", _ => {
        backend.getMatrix(matrixTypeInput.value).then(matrix => {
            const parsedMatrix = getParsedMatrix(matrix);

            matrixDisplay.innerText = parsedMatrix;
            downloadDataAsFile(parsedMatrix, matrixTypeInput.value + "-matrix");
        });
    });
});
