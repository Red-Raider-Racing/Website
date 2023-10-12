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

document.addEventListener("DOMContentLoaded", function() {
    const consentPopup = document.getElementById('consent-popup');
    if(consentPopup){
        const termsXbtn = document.querySelector('.buttonA#xaccept');

        const termsFn = () => {
            storageType.setItem('terms_accept', true); // Set terms_accept cookie
            consentPopup.classList.add('hidden');
        };

        termsXbtn.addEventListener('click', termsFn);

        if(!storageType.getItem('terms_accept')) {
            setTimeout(() => {
                consentPopup.classList.remove('hidden');
            }, 1000);
        }
    }

    const ad = document.querySelector('.ad');
    if(ad){
        const adXbtn = document.querySelector('.buttonA#xaccept');

        const adFn = () => {
            storageType.setItem('carshow_ad', true); // Set carshow cookie
            ad.classList.add('hidden');
        };

        adXbtn.addEventListener('click', adFn);

        if(!storageType.getItem('carshow_ad')) {
            setTimeout(() => {
                ad.classList.remove('hidden');
            }, 1000);
        }
    }
});