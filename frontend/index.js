import * as backend from "./modules/backend_connection.js"
import { handleFileSelect, getFileContent } from "./modules/file_uploader.js"
import { getParsedMatrix } from "./modules/matrix_parser.js"
import { downloadDataAsFile } from "./modules/downloader.js"

//api constants
const ALGORITHMS = [
    "Calculate Credibility Matrix",
    "Calculate Sorting",
    "Project Level",
    "Portfolio Leve"
];

const CONFIGS = [
    "Additional criteria parameters",
    "Credibility criteria",
    "Criteria directions",
    "Criteria hierarchy",
    "Criteria interactions",
    "Criteria parameters",
    "Performance matrix",
    "Use value function",
    "Veto thresholds for supercriteria",
    "Weights"
];

//DOM Ids
const IDs = {
    algorithmSelectorId : "algorithm-selector",
    executeButtonId : "execute-button",

    configSelectorId : "config-selector",
    configTextInputId : "config-text",
    configFileInputId : "config-file",
    sendTextButtonId : "send-text-button",
    sendFileButtonId : "send-file-button",
    getConfigButtonId : "get-config-button",

    outputSelectorId : "output-selector",
    getOutputButtonId : "get-output-button",
};

function visualizeRequestOutput(request, htmlElem, onSuccesMsg, onErrorMsg){
    const prevText = htmlElem.innerHTML;
    htmlElem.innerHTML = "...";
    request.then(_ => {
        htmlElem.innerHTML = onSuccesMsg;
        setTimeout(_ => {
            htmlElem.innerHTML = prevText;
        }, 800);
    }).catch(_ => {
        htmlElem.innerHTML = onErrorMsg;
        setTimeout(_ => {
            htmlElem.innerHTML = prevText;
        }, 1500);
    });
}

function fillSelectorOptions(selectorElem, options){
    for(const opt of options)
        selectorElem.innerHTML += `<option value=${opt}>${opt}</option>\n`;
}

document.addEventListener("DOMContentLoaded", _ => {
    const elems = Object.keys(IDs).reduce((output, id) => {
        output[IDs[id]] = document.getElementById(IDs[id]);
        return output;
    }, {});

    fillSelectorOptions(elems[IDs.algorithmSelectorId], ALGORITHMS);
    fillSelectorOptions(elems[IDs.configSelectorId], CONFIGS);

    elems[IDs.configFileInputId].addEventListener("change", handleFileSelect);

    elems[IDs.sendTextButtonId].addEventListener("click", _ => {
        const selectedConfig = elems[IDs.configSelectorId].value;
        const inputText = elems[IDs.configTextInputId].value;
        const request = backend.sendConfigFile(selectedConfig, inputText);
        visualizeRequestOutput(request, sendTextButton, "Enviado", "Fallido");
    });
    elems[IDs.sendFileButtonId].addEventListener("click", _ => {
        getFileContent().then(fileContent => {
            const selectedConfig = elems[IDs.configSelectorId].value;
            const request = backend.sendConfigFile(selectedConfig, fileContent);
            visualizeRequestOutput(request, elems[IDs.sendFileButtonId], "Enviado", "Fallido");
        }).catch(err => {
            console.log(err)
            const noEvent = new Promise(resolve => resolve());
            visualizeRequestOutput(noEvent,elems[IDs.sendFileButtonId], "Archivo No Seleccionado", "");   
        });
    });

    elems[IDs.getConfigButtonId].addEventListener("click", _ => {
        const selectedConfig = elems[IDs.configSelectorId].value;
        const request = backend.getConfigFile(selectedConfig);
        request.then(config => downloadDataAsFile(config, configTypeDropdown.value));
        visualizeRequestOutput(request, elems[IDs.getConfigButtonId], "Obtenido", "Fallido");
    });

    elems[IDs.executeButtonId].addEventListener("click", _ => {
        const request = backend.execute();
        request.then(response => {
            console.log(response);
        });
        visualizeRequestOutput(request, elems[IDs.executeButtonId], "Ejecutado", "Fallido");
    });

    elems[IDs.getOutputButtonId].addEventListener("click", _ => {
        const selectedAlgorithm = elems[IDs.algorithmSelectorId].value;
        const selectedOutput = elems[IDs.outputSelectorId].value;
        const request = backend.getMatrix(selectedOutput);
        request.then(output => {
            downloadDataAsFile(output, `${selectedOutput}-out-${selectedAlgorithm}`);
        });
        visualizeRequestOutput(request, elems[IDs.getOutputButtonId], "Obtenido", "Fallido");
    });
});
