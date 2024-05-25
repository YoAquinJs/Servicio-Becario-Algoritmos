import * as backend from "./modules/backend_connection.js"
import { requestFeedback } from "./modules/ui_feedback.js"
import { redirectTo } from "./modules/user_fetch.js"

//DOM Ids
const IDs = {
    loginUsername : "login-user-name",
    loginButton : "login",

    createUsername : "create-user-name",
    createUserButton : "create-user",

    deleteUsername : "delete-user-name",
    deleteUserButton : "delete-user",
};

document.addEventListener("DOMContentLoaded", _ => {
    const elems = Object.keys(IDs).reduce((output, id) => {
        output[IDs[id]] = document.getElementById(IDs[id]);
        return output;
    }, {});

    elems[IDs.loginButton].addEventListener("click", _ => {
        const username = elems[IDs.loginUsername].value;
        const request = backend.existsUser(username);
        requestFeedback(request, elems[IDs.loginButton], "", "Error");
        request.then(exists => {
            if (!exists){
                alert(`Usuario '${username}' no encontrado`)
                return;
            }
            redirectTo("app", username);
        });
    });
});