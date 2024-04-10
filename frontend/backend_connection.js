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
export function sendConfigFile(config_type, data){
    const param = new URLSearchParams({"config_data":data}).toString();
    return fetch(`${API_URI}/config/${config_type}?${param}`, {
        method : "POST",
    }).then(response => {
        if (!response.ok)
            throw new Error("No se pudo guardar la configuracion correctamente\n"+response.statusText);
        return response.json();
    })
    .then(data => {
        if (!data || !data.response)
            throw new Error("La respuesta no contiene la estructura esperada");
        return data.response;
    })
    .catch(error => {
        console.error(error);
    });
}

export function getConfigFile(config_type){
    return fetch(`${API_URI}/config/${config_type}`, {
        method : "GET",
    }).then(response => {
        if (!response.ok)
            return new Error("No se pudo acceder a la configuracion correctamente\n"+response.statusText);
        return response.json();
    })
    .then(data => {
        if (!data || !data.config)
            throw new Error("La respuesta no contiene la estructura esperada");
        return data.config;
    })
    .catch(error => {
        console.error(error);
    });
}

export function getMatrix(matrix_type){
    return fetch(`${API_URI}/matrix/${matrix_type}`, {
        method : "GET",
    }).then(response => {
        if (!response.ok)
            return new Error("No se pudo acceder a la matriz correctamente\n"+response.statusText);
        return response.json();
    })
    .then(data => {
        if (!data || !data.matrix)
            throw new Error("La respuesta no contiene la estructura esperada");
        return data;
    })
    .catch(error => {
        console.error(error);
    });
}

export function execute(){
    return fetch(`${API_URI}/execute`, {
        method : "POST",
    }).then(response => {
        if (!response.ok)
            return new Error("No se pudo ejecutar");
        return response.json();
    })
    .then(data => {
        if (!data || !data.response)
            throw new Error("La respuesta no contiene la estructura esperada\n"+response.statusText);
        return data.response;
    })
    .catch(error => {
        console.error(error);
    });
}