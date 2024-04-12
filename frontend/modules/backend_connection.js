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

//Api Calls
export async function sendConfigFile(config_type, data){
    const param = new URLSearchParams({"config_data":data}).toString();
    const response = await fetch(`${API_URI}/config/${config_type}?${param}`, {method : "POST",});
    if (!response.ok)
        throw new Error("No se pudo guardar la configuracion correctamente\n"+response.statusText);

    const parsedResponsed = await response.json(); 
    if (!parsedResponsed || !parsedResponsed.response)
        throw new Error("La respuesta no contiene la estructura esperada");

    return parsedResponsed.response;
}

export async function getConfigFile(config_type){
    const response = await fetch(`${API_URI}/config/${config_type}`, {method : "GET",});
    if (!response.ok)
        throw new Error("No se pudo acceder a la configuracion correctamente\n"+response.statusText);

    const parsedResponsed = await response.json(); 
    if (!parsedResponsed || !parsedResponsed.config)
        throw new Error("La respuesta no contiene la estructura esperada");

    return parsedResponsed.config;
}

export async function getMatrix(matrix_type){
    const response = await fetch(`${API_URI}/matrix/${matrix_type}`, {method : "GET",});
    if (!response.ok)
        throw new Error("No se pudo acceder a la matriz correctamente\n"+response.statusText);

    const parsedResponsed = await response.json(); 
    if (!parsedResponsed || !parsedResponsed.matrix)
        throw new Error("La respuesta no contiene la estructura esperada");

    return parsedResponsed.matrix;
}

export async function execute(){
    const response = await fetch(`${API_URI}/execute`, {method : "POST",});
    if (!response.ok)
        throw new Error("No se pudo ejecutar correctamente\n"+response.statusText);

    const parsedResponsed = await response.json(); 
    if (!parsedResponsed || !parsedResponsed.response)
        throw new Error("La respuesta no contiene la estructura esperada");

    return parsedResponsed.response;
}