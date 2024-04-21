const API_URI = 'http://127.0.0.1:8000'

//Api on start validation
fetch(`${API_URI}/`, {
    method : "GET"
}).then(response => {
    if (!response.ok){
        console.error('conexion con backend fallida');
        console.error({'error code':response.status});
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
        if (typeof responseVal !== typeof expectedVal)
            return false;
        if (typeof expectedVal === "object" && !isValidResponse(responseVal, expectedVal))
            return false;
    }

    return true;
}

//Api Calls
export async function sendConfigFile(config_type, data){
    const param = new URLSearchParams({"config_data":data}).toString();
    const response = await fetch(`${API_URI}/config/${config_type}?${param}`, {method : "POST",});
    if (!response.ok)
        throw new Error("No se pudo guardar la configuracion correctamente\n"+response.statusText);

    const parsedResponse = await response.json(); 
    if (!isValidResponse(parsedResponse, {"response":""}))
        throw new Error("La respuesta no contiene la estructura esperada");

    return parsedResponse.response;
}

export async function getConfigFile(config_type){
    const response = await fetch(`${API_URI}/config/${config_type}`, {method : "GET",});
    if (!response.ok)
        throw new Error("No se pudo acceder a la configuracion correctamente\n"+response.statusText);

    const parsedResponse = await response.json();
    if (!isValidResponse(parsedResponse, {"config":""}))
        throw new Error("La respuesta no contiene la estructura esperada");

    return parsedResponse.config;
}

export async function getMatrix(matrix_type){
    const response = await fetch(`${API_URI}/matrix/${matrix_type}`, {method : "GET",});
    if (!response.ok)
        throw new Error("No se pudo acceder a la matriz correctamente\n"+response.statusText);

    const parsedResponse = await response.json(); 
    if (!isValidResponse(parsedResponse, {"matrix":""}))
        throw new Error("La respuesta no contiene la estructura esperada");

    return parsedResponse.matrix;
}

export async function execute(){
    const response = await fetch(`${API_URI}/execute`, {method : "POST",});
    if (!response.ok)
        throw new Error("No se pudo ejecutar correctamente\n"+response.statusText);

    const parsedResponse = await response.json(); 
    if (!isValidResponse(parsedResponse, {"response":""}))
        throw new Error("La respuesta no contiene la estructura esperada");

    return parsedResponse.response;
}