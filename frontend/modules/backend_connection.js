import { HttpError, ResponseFormatError } from "./errors.js"

const API_URI = "http://127.0.0.1:8000"

//Api on start validation
fetch(`${API_URI}/`, {
    method : "GET"
}).then(response => {
    if (!response.ok){
        console.error("conexion con backend fallida");
        console.error({"error code":response.status});
    }
    return response.json();
})
.then(_ => {})
.catch(error => {
    console.error(error);
});

//Throws an expcetion if the format of the response does not match the expected one
//Otherwiise does nothing and returns undefined
function validateResponseFormat(response, expectedFormat) {
    if (!response || !expectedFormat || typeof response !== typeof expectedFormat)
        throw new ResponseFormatError("Null or undefined parameters");

    const expected = Object.keys(expectedFormat);
    if (Object.keys(response).length !== expected.length)
        throw new ResponseFormatError("Invalid response format structure");

    for (let key of expected) {
        if (!response.hasOwnProperty(key))
            throw new ResponseFormatError("Invalid response format structure");

        const responseVal = response[key];
        const expectedVal = expectedFormat[key];
        if (expectedVal === undefined)
            continue;
        if (typeof expectedVal !== typeof responseVal)
            throw new ResponseFormatError(`Invalid attribute "${key}" type`);
        if (typeof expectedVal === "object")
            validateResponseFormat(responseVal, expectedVal);
    }
}

//Api Calls
export async function getConfigFile(algorithmType, configType){
    const fetchURI = `${API_URI}/config/${algorithmType}/${configType}`;

    const response = await fetch(fetchURI, {method:"GET"});
    const parsedResponse = await response.json();

    if (!response.ok)
        throw new HttpError(response.status, parsedResponse.detail);

    validateResponseFormat(parsedResponse, {"config":""});

    return parsedResponse.config;
}

export async function modifyConfig(algorithmType, configType, data){
    const param = new URLSearchParams({"config_data":data}).toString();
    const fetchURI = `${API_URI}/config/${algorithmType}/${configType}?${param}`;

    const response = await fetch(fetchURI, {method:"POST"});
    const parsedResponse = await response.json(); 

    if (!response.ok)
        throw new HttpError(response.status, parsedResponse.detail);

    validateResponseFormat(parsedResponse, {"response":""});

    return parsedResponse.response;
}

export async function getOutput(algorithmType, outputType){
    const fetchURI = `${API_URI}/output/${algorithmType}/${outputType}`;

    const response = await fetch(fetchURI, {method:"GET"});
    const parsedResponse = await response.json(); 

    if (!response.ok)
        throw new HttpError(response.status, parsedResponse.detail);

    validateResponseFormat(parsedResponse, {"output":undefined});

    return parsedResponse.output;
}

export async function execute(algorithmType){
    const fetchURI = `${API_URI}/execute/${algorithmType}`;

    const response = await fetch(fetchURI, {method:"POST"});
    const parsedResponse = await response.json();

    if (!response.ok)
        throw new HttpError(response.status, parsedResponse.detail);

    validateResponseFormat(parsedResponse, {"response":""});

    return parsedResponse.response;
}