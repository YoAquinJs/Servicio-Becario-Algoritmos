export const USERNAME_KEY = "username";

export function getUser(){
    return sessionStorage.getItem(USERNAME_KEY);
}

export function redirectTo(html, username){
    sessionStorage.setItem(USERNAME_KEY, username);

    const appPage = `${html}.html`;
    window.location.href = appPage;
}
