import * as backend from "./modules/backend_connection.js"
import { handleFileSelect, getFileContent } from "./modules/file_uploader.js"
import { downloadDataAsFile } from "./modules/downloader.js"
import { requestFeedback } from "./modules/ui_feedback.js"
import { visualizeOutput } from "./modules/output_visualizer.js"

const ALGORITHMS = [
    "Calculate credibility matrix",
    "Calculate sorting",
    "Project level",
    "Portfolio level"
];

const ALGORITHM_COL_CSS_VAR = "--algorithm-color";
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
    "Weights",
    "Sorting criteria"
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

    outputTableContainer : "output-table",
};

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
        elems[IDs.outputTableContainer].innerHTML = "";

        const selectedAlgorithm = elems[IDs.algorithmSelector].value;
        elems[IDs.algorithmTitle].textContent = selectedAlgorithm;

        const color = algorithmPageColors[selectedAlgorithm];
        document.documentElement.style.setProperty(ALGORITHM_COL_CSS_VAR, color);
    });

    fillSelectorOptions(elems[IDs.algorithmSelector], ALGORITHMS);
    fillSelectorOptions(elems[IDs.configSelector], CONFIGS);

    elems[IDs.configFileInput].addEventListener("change", handleFileSelect);

    elems[IDs.sendTextButton].addEventListener("click", _ => {
        const selectedAlgorithm = elems[IDs.algorithmSelector].value;
        const selectedConfig = elems[IDs.configSelector].value;
        const inputText = elems[IDs.configTextInput].value;
        const request = backend.modifyConfig(selectedAlgorithm, selectedConfig, inputText);
        requestFeedback(request, elems[IDs.sendTextButton], "Enviado", "Fallido");
    });
    elems[IDs.sendFileButton].addEventListener("click", _ => {
        getFileContent().then(fileContent => {
            const selectedAlgorithm = elems[IDs.algorithmSelector].value;
            const selectedConfig = elems[IDs.configSelector].value;
            const request = backend.modifyConfig(selectedAlgorithm, selectedConfig, fileContent);
            requestFeedback(request, elems[IDs.sendFileButton], "Enviado", "Fallido");
        }).catch(_ => {
            const noEvent = new Promise(resolve => resolve());
            requestFeedback(noEvent,elems[IDs.sendFileButton], "Archivo No Seleccionado", "");   
        });
    });

    elems[IDs.getConfigButton].addEventListener("click", _ => {
        const selectedAlgorithm = elems[IDs.algorithmSelector].value;
        const selectedConfig = elems[IDs.configSelector].value;
        const request = backend.getConfigFile(selectedAlgorithm, selectedConfig);
        request.then(config => downloadDataAsFile(config, selectedConfig));
        requestFeedback(request, elems[IDs.getConfigButton], "Obtenido", "Fallido");
    });

    elems[IDs.executeButton].addEventListener("click", _ => {
        elems[IDs.outputTableContainer].innerHTML = "";

        const selectedAlgorithm = elems[IDs.algorithmSelector].value;
        const request = backend.execute(selectedAlgorithm);

        request.then(response => {
            alert(response);
        }); 
        requestFeedback(request, elems[IDs.executeButton], "Ejecutado", "Fallido");
    });

    elems[IDs.getOutputButton].addEventListener("click", _ => {
        const selectedAlgorithm = elems[IDs.algorithmSelector].value;
        const selectedOutput = elems[IDs.outputSelector].value;
        
        const request = backend.getOutput(selectedAlgorithm, selectedOutput);
        request.then(output => {
            downloadDataAsFile(output, `${selectedOutput}-out-${selectedAlgorithm}`);
            visualizeOutput(output, elems[IDs.outputTableContainer]);
        });

        requestFeedback(request, elems[IDs.getOutputButton], "Obtenido", "Fallido");
    });
});
