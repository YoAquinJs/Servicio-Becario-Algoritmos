import * as backend from "./modules/backend_connection.js"
import { handleFileSelect, getFileContent } from "./modules/file_uploader.js"
import { downloadDataAsFile } from "./modules/downloader.js"
import { HttpError, ResponseFormatError } from "./modules/errors.js"
const ALGORITHMS = [
    "Calculate credibility matrix",
    "Calculate sorting",
    "Project level",
    "Portfolio level"
];

const algorithmCols = ["#8495b9","#c9b14a","#66cc99","#aa6fd1"]

const algorithmPageColors = ALGORITHMS.reduce((acc, key, idx) => {
    acc[key] = algorithmCols[idx];
    return acc;
}, {});

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
    algorithmTitle : "algorithm-title",
    algorithmSelector : "algorithm-selector",
    executeButton : "execute-button",

    configSelector : "config-selector",
    configTextInput : "config-text",
    configFileInput : "config-file",
    sendTextButton : "send-text-button",
    sendFileButton : "send-file-button",
    getConfigButton : "get-config-button",

    outputSelector : "output-selector",
    getOutputButton : "get-output-button",
};

function visualizeRequestOutput(request, htmlElem, onSuccesMsg, onErrorMsg){
    const prevText = htmlElem.innerHTML;
    htmlElem.disabled = true;
    htmlElem.innerHTML = "...";

    request.then(_ => {
        htmlElem.innerHTML = onSuccesMsg;
        setTimeout(_ => {
            htmlElem.innerHTML = prevText;
            htmlElem.disabled = false;
        }, 800);
    }).catch(error => {
        if (error instanceof HttpError)
            alert(error.detail);

        htmlElem.innerHTML = onErrorMsg;
        setTimeout(_ => {
            htmlElem.innerHTML = prevText;
            htmlElem.disabled = false;
        }, 1500);
    });
}

function fillSelectorOptions(selectorElem, options){
    for(const opt of options)
        selectorElem.innerHTML += `<option value="${opt}">${opt}</option>\n`;
    selectorElem.value = options[0];
    selectorElem.dispatchEvent(new Event("change"));
}

document.addEventListener("DOMContentLoaded", _ => {
    const elems = Object.keys(IDs).reduce((output, id) => {
        output[IDs[id]] = document.getElementById(IDs[id]);
        return output;
    }, {});

    elems[IDs.algorithmSelector].addEventListener("change", _ => {
        const selectedAlgorithm = elems[IDs.algorithmSelector].value;
        elems[IDs.algorithmTitle].textContent = selectedAlgorithm;
        const color = algorithmPageColors[selectedAlgorithm];
        const cssAlgorithmColor = "--algorithm-color";
        document.documentElement.style.setProperty(cssAlgorithmColor, color);
    });

    fillSelectorOptions(elems[IDs.algorithmSelector], ALGORITHMS);
    fillSelectorOptions(elems[IDs.configSelector], CONFIGS);

    elems[IDs.configFileInput].addEventListener("change", handleFileSelect);

    elems[IDs.sendTextButton].addEventListener("click", _ => {
        const selectedAlgorithm = elems[IDs.algorithmSelector].value;
        const selectedConfig = elems[IDs.configSelector].value;
        const inputText = elems[IDs.configTextInput].value;
        const request = backend.modifyConfig(selectedAlgorithm, selectedConfig, inputText);
        visualizeRequestOutput(request, elems[IDs.sendTextButton], "Enviado", "Fallido");
    });
    elems[IDs.sendFileButton].addEventListener("click", _ => {
        getFileContent().then(fileContent => {
            const selectedAlgorithm = elems[IDs.algorithmSelector].value;
            const selectedConfig = elems[IDs.configSelector].value;
            const request = backend.modifyConfig(selectedAlgorithm, selectedConfig, fileContent);
            visualizeRequestOutput(request, elems[IDs.sendFileButton], "Enviado", "Fallido");
        }).catch(_ => {
            const noEvent = new Promise(resolve => resolve());
            visualizeRequestOutput(noEvent,elems[IDs.sendFileButton], "Archivo No Seleccionado", "");   
        });
    });

    elems[IDs.getConfigButton].addEventListener("click", _ => {
        const selectedAlgorithm = elems[IDs.algorithmSelector].value;
        const selectedConfig = elems[IDs.configSelector].value;
        const request = backend.getConfigFile(selectedAlgorithm, selectedConfig);
        request.then(config => downloadDataAsFile(config, selectedConfig));
        visualizeRequestOutput(request, elems[IDs.getConfigButton], "Obtenido", "Fallido");
    });

    elems[IDs.executeButton].addEventListener("click", _ => {
        const selectedAlgorithm = elems[IDs.algorithmSelector].value;
        const request = backend.execute(selectedAlgorithm);
        request.then(response => {
            console.log(response);
        });
        visualizeRequestOutput(request, elems[IDs.executeButton], "Ejecutado", "Fallido");
    });

    elems[IDs.getOutputButton].addEventListener("click", _ => {
        const selectedAlgorithm = elems[IDs.algorithmSelector].value;
        const selectedOutput = elems[IDs.outputSelector].value;
        const request = backend.getOutput(selectedAlgorithm, selectedOutput);
        request.then(output => {
            downloadDataAsFile(output, `${selectedOutput}-out-${selectedAlgorithm}`);
        });
        visualizeRequestOutput(request, elems[IDs.getOutputButton], "Obtenido", "Fallido");
    });
});
