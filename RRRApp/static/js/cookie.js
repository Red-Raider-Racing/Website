//Cookies Popup Implementation for new users
const cookieStorage = {
    getItem: (key) => {
        const cookies = document.cookie
            .split(';')
            .map(cookie => cookie.split('='))
            .reduce((acc, [key, value]) => ({ ...acc, [key.trim()]: value }), {});
        return cookies[key]
    },
    setItem: (key, value, daysToExpire = 30) => {
        const date = new Date();
        date.setTime(date.getTime() + (daysToExpire * 24 * 60 * 60 * 1000));
        const expires = `expires=${date.toUTCString()}`;
        const cookieOptions = `SameSite=Lax`;
        document.cookie = `${key}=${value}; ${expires}; ${cookieOptions}; path=/`;
    },
};

//Can change into any storage needed session, local, etc.
const storageType = cookieStorage;
const consentPropertyName = 'terms_accept';

//Helper Functions to determine whether popup will be shown or not
//References to local storage
const shouldShowPopup = () => !storageType.getItem(consentPropertyName);
const saveToStorage = () => storageType.setItem(consentPropertyName, true);

document.addEventListener("DOMContentLoaded", function() {
    const consentPopup = document.getElementById('consent-popup');
    if(consentPopup){
        const xBtn = document.querySelector('.buttonA#xaccept');

        const acceptFn = () => {
            saveToStorage(storageType);
            consentPopup.classList.add('hidden');
        };

        xBtn.addEventListener('click', acceptFn);

        if(shouldShowPopup()) {
            setTimeout(() => {
                consentPopup.classList.remove('hidden');
            }, 1000);
        }
    }
});