api_uri = 'http://127.0.0.1:8000'

fetch(api_uri+'/', {
    method : 'GET'
})
.then(response => {
    if (!response.ok)
        console.error('conexion con backend fallida');
        console.error({'error code':response.status});
    return response.json();
})
.then(_ => {})
.catch(error => {
    console.error(error);
});

function sendConfigFile(){
    fetch(api_uri+'/')
    .then(response => {
        if (!response.ok)
            console.error('failed to connect with backend');
            console.error({'error code':response.status});
        return response.json();
    })
    .then(_ => {})
    .catch(error => {
        console.error(error);
    });
}
