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

function isValidResponse(response, expectedStruct) {
    if (!response || !expectedStruct || typeof response !== typeof expectedStruct)
        return false;

    const expected = Object.keys(expectedStruct);
    if (Object.keys(response).length !== expected.length)
        return false;

    for (let key of expected) {
        if (!response.hasOwnProperty(key))
            return false;
        
        const responseVal = response[key];
        const expectedVal = expectedStruct[key];
        if (expectedVal === undefined)
            continue;
        if (typeof expectedVal !== typeof responseVal)
            return false;
        if (typeof expectedVal === "object" && !isValidResponse(responseVal, expectedVal))
            return false;
    }

    return true;
}

//Api Calls
export async function getConfigFile(algorithmType, configType){
    const fetchURI = `${API_URI}/config/${algorithmType}/${configType}`;
    const response = await fetch(fetchURI, {method:"GET"});
    
    if (!response.ok)
        throw new Error("Failed request: \n"+response.statusText);

    const parsedResponse = await response.json();
    if (!isValidResponse(parsedResponse, {"config":""}))
        throw new Error("Response does not contain expected structure");

    return parsedResponse.config;
}

export async function modifyConfig(algorithmType, configType, data){
    const param = new URLSearchParams({"config_data":data}).toString();
    const fetchURI = `${API_URI}/config/${algorithmType}/${configType}?${param}`;
    const response = await fetch(fetchURI, {method:"POST"});
    
    if (!response.ok)
        throw new Error("Failed request: \n"+response.statusText);

    const parsedResponse = await response.json(); 
    if (!isValidResponse(parsedResponse, {"response":""}))
        throw new Error("Response does not contain expected structure");

    return parsedResponse.response;
}

export async function getOutput(algorithmType, outputType){
    const fetchURI = `${API_URI}/output/${algorithmType}/${outputType}`;
    const response = await fetch(fetchURI, {method:"GET"});
    
    if (!response.ok)
        throw new Error("Failed request: \n"+response.statusText);

    const parsedResponse = await response.json(); 
    if (!isValidResponse(parsedResponse, {"matrix":undefined}))
        throw new Error("Response does not contain expected structure");

    return parsedResponse.matrix;
}

export async function execute(algorithmType){
    const fetchURI = `${API_URI}/execute/${algorithmType}`;
    const response = await fetch(fetchURI, {method:"POST"});
    
    if (!response.ok)
        throw new Error("Failed request: \n"+response.statusText);

    const parsedResponse = await response.json(); 
    if (!isValidResponse(parsedResponse, {"response":""}))
        throw new Error("Response does not contain expected structure");

    return parsedResponse.response;
}