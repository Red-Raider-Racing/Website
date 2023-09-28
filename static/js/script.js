/** 
 * Author: Carson Spaniel
 * Date: 8/15/23
*/

// Function for when the page is loaded. Initialization stuff
document.addEventListener("DOMContentLoaded", function() {
    const questions = document.querySelectorAll(".faq");
    
    // Finds all the questions in the FAQ page and listens to see if it is clicked on
    questions.forEach(question => {
        question.addEventListener("click", function() {
            this.classList.remove("active");
            const answer = this.nextElementSibling;
            
            // Hide answer if it is selected
            if (answer.style.display === "block") {
                answer.style.opacity = 0;
                answer.style.display = "none";
            }
            else {
                // Hide answer if another answer is selected
                questions.forEach(q => {
                    if (q !== this) {
                        q.classList.remove("active");
                        const otherAnswer = q.nextElementSibling;
                        otherAnswer.style.opacity = 0;
                        otherAnswer.style.display = "none";
                    }
                });
                
                this.classList.add("active"); // Highlight answer
                answer.style.display = "block"; // Show answer

                // Fade answer in
                setTimeout(() => {
                    answer.style.opacity = 1;
                }, 10);
            }
        });
    });

    // Function to check if an element is coming into view (intersection)
    function isElementIntersecting(entry) {
        return entry.isIntersecting || entry.intersectionRatio > 0;
    }

    // Function to handle the intersection
    function handleIntersection(entries, observer) {
        entries.forEach(function(entry) {
            if (isElementIntersecting(entry)) {
                entry.target.classList.add("visible");
                // Stop observing the element after it becomes visible
                observer.unobserve(entry.target);
            }
        });
    }

    // Create the Intersection Observer
    const observer = new IntersectionObserver(handleIntersection, {
        root: null,
        rootMargin: "0px",
        threshold: 0.1, // The percentage of the element that must be visible to trigger the intersection
    });


    // Looks for members
    const members = document.querySelectorAll(".member");
    members.forEach(function(member) {
        observer.observe(member);
    });

    // Looks for benefits
    const benefits = document.querySelectorAll(".benefit");
    benefits.forEach(function(benefit) {
        observer.observe(benefit);
    });

    // If benefit has been visited stop flipping them
    benefits.forEach(card => {
        card.addEventListener('mouseenter', () => {
            benefitTitles.forEach(benefitTitle=>{
                benefitTitle.classList.add('viewed');
            });
        });
        card.addEventListener('click', () => {
            benefitTitles.forEach(benefitTitle=>{
                benefitTitle.classList.add('viewed');
            });
            card.classList.toggle('flipped');
        });
    });

    const benefitTitles = document.querySelectorAll(".benefitTitle");
    setTimeout(()=>{
        for (let i = 0; i < benefits.length; i++) {
            setTimeout(() => {
                if (!benefits[i].classList.contains('flipped')) {
                    shakeBenefits(benefitTitles[i]);
                }
            }, 300 * (i+1));
        }
    },2500);

    // Looks for cars
    const cars = document.querySelectorAll(".car");
    cars.forEach(function(car) {
        observer.observe(car);
    });

    // Looks for cars
    const carsIMG = document.querySelectorAll(".carIMG");
    carsIMG.forEach(function(carIMG) {
        observer.observe(carIMG);
    });

    // Zooms into car
    if (carsIMG) {
        carsIMG.forEach((car) => {
          car.addEventListener('click', () => {
            car.classList.toggle('zoom');
      
            carsIMG.forEach((otherCar) => {
              if (otherCar !== car) {
                otherCar.classList.remove('zoom');
              }
            });
          });
        });
    }

    // Looks for sponsors
    const sponsors = document.querySelectorAll(".sponsor");
    sponsors.forEach(function(sponsor) {
        observer.observe(sponsor);
    });

    // Grabs the join variable
    var joinParam = GetURLParameter('join');
    if (joinParam){
        showAnswer('join');
    }

    // Grabs the fsae variable
    var fsaeParam = GetURLParameter('fsae');
    if (fsaeParam){
        showAnswer('fsae');
    }

    // Grabs the success variable
    var successParam = GetURLParameter('success');
    if (successParam){
        var message;
        if (successParam == 1){
            message = 'sent';
        }
        else{
            message = 'fail';
        }
        showSent(message);
    }

    updateLoaderTurns();
});

function updateLoaderTurns(){
    // Get the screen width and update the CSS variable
    const screenWidth = window.innerWidth;
    document.documentElement.style.setProperty('--screen-width', `${screenWidth}px`);

    // Calculate the number of turns based on the screen width
    const numberOfTurns = screenWidth / 200; // You can adjust this ratio as needed
    document.documentElement.style.setProperty('--number-of-turns', numberOfTurns);
    
}

// Function to update the padding of the "main" element based on the height of the "nav" element
function updateMainPadding() {
    const logo = document.querySelector(".logo-image")
    const logoCon = document.querySelector(".logo")
    const navMain = document.querySelector(".navMain")
    const altNav = document.querySelector(".altNav")
    const menuButton = document.querySelector(".menuButton");
    const header = document.querySelector('header');
    const menu = document.querySelector(".dropdown-content");
    const menuCon = document.querySelector(".dropdown");
    const headerBackground = document.querySelector(".headerBackground");

    const viewportWidth = window.innerWidth;
    const viewportHeight = window.innerHeight;

    // Close the menu
    if (menu.style.display === "block") {
        menu.style.display = "none";
        menuButton.style.position = "relative";
        menuButton.style.top = "";
        menuButton.innerHTML = "&#9776;";
        menuButton.style.marginLeft = "0px";
        menuButton.style.marginTop = "0px";
        header.style.height = "";
        logoCon.style.display = 'flex';

        // Enable scrolling
        enableScrolling();
    } 

    // Add responsiveness based on width of screen
    if(viewportWidth <= 1000 ){
        logo.style.height = '40px';
        logoCon.style.padding = '0px';
        navMain.style.display = 'none';
        altNav.style.display = 'flex';
        if (headerBackground != null){
            headerBackground.style.display = 'none';
        }
    }
    else{
        logo.style.height = '';
        navMain.style.display = 'flex';
        altNav.style.display = 'none';
        logoCon.style.padding = '10px';
        if (headerBackground != null){
            headerBackground.style.display = 'block';
        }
    }

    if (viewportHeight <= 1100) {
        menuCon.classList.add('small-screen');
        menu.classList.add('small-screen');
    } 
    else {
        menuCon.classList.remove('small-screen');
        menu.classList.remove('small-screen');
        menuButton.style.marginLeft = "";
    }

    const mainElement = document.querySelector(".pageTitle");
    if (mainElement){
        mainElement.style.paddingTop = `${header.clientHeight+80}px`;
    }
}

// Initial update when the DOM is ready
document.addEventListener("DOMContentLoaded", updateMainPadding);

// Update padding on window resize
window.addEventListener("resize", ()=>{
    updateMainPadding();
    updateLoaderTurns();
});

document.addEventListener("click", function(event) {
    const header = document.querySelector('header');
    const menu = document.querySelector(".dropdown-content");
    if (!header.contains(event.target)) {
        menu.style.display = "none";
    }
});

// Function to toggle the display of the dropdown content
function toggleMenu() {
    const menu = document.querySelector(".dropdown-content");
    const menuCon = document.querySelector(".dropdown");
    const menuButton = document.querySelector(".menuButton");
    const header = document.querySelector('header');
    const logo = document.querySelector(".logo");

    if (menu.style.display === "flex") {
        // Close the menu
        header.style.backgroundColor = "";
        header.style.boxShadow = "";
        menu.style.display = "none";
        menuButton.style.position = "relative";
        menuButton.style.top = "";
        menuButton.innerHTML = "&#9776;";
        menuButton.style.marginLeft = "0px";
        menuButton.style.marginTop = "0px";
        header.style.height = "";
        logo.style.display = 'flex';
        menuCon.style.top = "";
        menuCon.style.left = "";
        menuCon.style.right = "";

        enableScrolling();
    } 
    else {
        // Open the menu
        header.style.backgroundColor = "var(--primary-faded-color)";
        header.style.boxShadow = "var(--shadow)";
        menuButton.style.position = "absolute";
        menuButton.style.top = "30px";
        menu.style.display = "flex";
        menuButton.innerHTML = "&#x2715;";
        menuButton.style.marginLeft = "200px";
        menuButton.style.marginTop = "-100px";
        header.style.height = "100%";
        logo.style.display = 'none';
        menuCon.style.top = "100px";
        menuCon.style.left = "0";
        menuCon.style.right = "0";

        disableScrolling();
    }
    document.body.style.left = '0px';
    document.body.style.right = '0px';
}

// Function to disable the scrolling
function disableScrolling() {
    const header = document.querySelector('header');
    const scrollY = window.scrollY;

    header.removeAttribute('id');
    document.body.style.position = "fixed";
    document.body.style.top = `${-scrollY}px`;
}

// Function to enable the scrolling
function enableScrolling() {
    const header = document.querySelector('header');
    const scrollY = parseInt(document.body.style.top);

    header.setAttribute('id', 'mainHeader');
    document.body.style.position = "";
    document.body.style.top = "";
    window.scrollTo(0, -scrollY); // Scroll back down to where screen was at
}

let prevScrollPos = window.pageYOffset; // Previous scroll position

// Function to hide/show the header on scroll
window.onscroll = function() {
    const currentScrollPos = window.pageYOffset;
    const header = document.getElementById("mainHeader");
    const viewportWidth = window.innerWidth;
    if ((viewportWidth*.5)>300){
        width = 300;
    }
    else{
        width = viewportWidth*.5;
    }

    if (header){
        // Check if scrolled more than width amount of pixels
        if (currentScrollPos > width) {
            if (prevScrollPos > currentScrollPos) {
                header.style.top = "-5px";
            } else {
                header.style.top = `-${header.clientHeight}px`; // Hide header
            }
        }

        // Keep header visible for the first few hundred pixels
        else {
            header.style.top = "0";
        }

        prevScrollPos = currentScrollPos;
    }
};

window.addEventListener('scroll', function () {
    const scrollY = window.scrollY; // See where the scroll is at

    // ------------ Parallax stuff------------
    const parallaxBackground = document.querySelector('.coverIMG');
    const pageTitle = document.querySelector('.pageTitle');
    if (parallaxBackground != null){ // Check to see if the parallax background is on this page
        parallaxBackground.style.transform = `translateY(${scrollY * 0.5}px)`; // Perform the parallax effect
    }
    pageTitle.style.transform = `translateY(-${scrollY * .2}px)`;

    // ------------ transparent top stuff------------
    const navElement = document.querySelector('header'); // Check if scroll position is at the top of the page (scrollY is zero)
    if (scrollY === 0 && document.body.style.top >= 0) {
        // Scroll is at the top, make the header clear and remove box shadow
        navElement.style.backgroundColor = "transparent";
        navElement.style.boxShadow = "none";
    } else {
        // Scroll is not at the top, set background color and box shadow as needed
        navElement.style.backgroundColor = "var(--primary-faded-color)";
        navElement.style.boxShadow = "var(--shadow)";
    }

    // Rest of your scroll event handling code...
});

// Function to grab all URL variables
function GetURLParameter(sParam) {
    var sPageURL = window.location.search.substring(1);
    var sURLVariables = sPageURL.split('&');
    for (var i = 0; i < sURLVariables.length; i++) 
    {
        var sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == sParam) 
        {
            return sParameterName[1];
        }
    }
}

// Function to show "How to join" answer
function showAnswer(section) {
    const answer = document.getElementById(section+"-answer");
    const question = document.getElementById(section+'-question');
    question.classList.add("active");
    answer.style.display = 'block';
    answer.style.opacity = '1';
}

// Function to show that the message sent or failed
function showSent(message) {
    console.log(message);
    const send = document.getElementById(message);
    send.style.display = 'block';
}

// Function to show the loading screen
function showLoading() {
    const loader = document.getElementById('loading');
    loader.classList.add('load');
    loader.style.display = 'block';
}

// Function to show character count for the email message
function updateCharacterCount() {
    const textarea = document.getElementById('message');
    const characterCount = textarea.value.length;
    const maxCharacters = parseInt(textarea.getAttribute('maxlength'));
    const remainingCharacters = maxCharacters - characterCount;
    const characterCountDisplay = document.getElementById('character-count');
    characterCountDisplay.textContent = `Characters remaining: ${remainingCharacters}`;
}

// Function to clean the input to protect against code injection
function sanitizeInput(inputField) {
    const inputValue = inputField.value;
    const sanitizedValue = DOMPurify.sanitize(inputValue, { ALLOWED_TAGS: ['p', 'br'] });

    const displayValue = sanitizedValue.replace(/&lt;/g, '<').replace(/&gt;/g, '>');
    inputField.value = displayValue;
}

// Function to shake the benefits in a wave pattern every 5 seconds until viewed
function shakeBenefits(benefitTitle){
    if (!benefitTitle.classList.contains('viewed')){
        benefitTitle.classList.add('benefitAnimate');
        setTimeout(() => {
            benefitTitle.classList.remove('benefitAnimate');
            setTimeout(() => {
                shakeBenefits(benefitTitle);
            }, 5000);
        }, 200);
    }
}