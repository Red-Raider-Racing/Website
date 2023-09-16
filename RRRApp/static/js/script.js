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
            const answer = this.nextElementSibling;
            
            // Hide answer if it is selected
            if (answer.style.display === "block") {
                answer.style.opacity = 0;

                // Fade out the answer
                setTimeout(() => {
                    answer.style.display = "none";
                }, 20);
            }
            else {
                // Hide answer if another answer is selected
                questions.forEach(q => {
                    if (q !== this) {
                        q.classList.remove("active");
                        const otherAnswer = q.nextElementSibling;
                        otherAnswer.style.opacity = 0;
                        setTimeout(() => {
                            otherAnswer.style.display = "none";
                        }, 20);
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

    // Looks for cars
    const cars = document.querySelectorAll(".car");
    cars.forEach(function(car) {
        observer.observe(car);
    });

    // Grabs the join variable
    var joinParam = GetURLParameter('join');
    if (joinParam){
        showJoin();
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

});

// Function to update the padding of the "main" element based on the height of the "nav" element
function updateMainPadding() {
    const logo = document.querySelector(".logo-image")
    const logoCon = document.querySelector(".logo")
    const navMain = document.querySelector(".navMain")
    const altNav = document.querySelector(".altNav")
    const menuButton = document.querySelector(".menuButton");
    const header = document.getElementById("mainHeader");
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

    const navElement = document.getElementById("mainHeader");
    const mainElement = document.querySelector(".pageTitle");
    mainElement.style.paddingTop = `${navElement.clientHeight+80}px`;
}

// Initial update when the DOM is ready
document.addEventListener("DOMContentLoaded", updateMainPadding);

// Update padding on window resize
window.addEventListener("resize", updateMainPadding);

document.addEventListener("click", function(event) {
    const header = document.getElementById("mainHeader");
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
    const header = document.getElementById("mainHeader");
    const logo = document.querySelector(".logo");
    const navElement = document.getElementById("mainHeader");

    if (menu.style.display === "flex") {
        // Close the menu
        navElement.style.backgroundColor = "";
        navElement.style.boxShadow = "";
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
        navElement.style.backgroundColor = "var(--primary-faded-color)";
        navElement.style.boxShadow = "var(--shadow)";
        menuButton.style.position = "absolute";
        menuButton.style.top = "30px";
        menu.style.display = "flex";
        menuButton.innerHTML = "&#10006;";
        menuButton.style.marginLeft = "200px";
        menuButton.style.marginTop = "-120px";
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
    const scrollY = window.scrollY;
    document.body.style.position = "fixed";
    document.body.style.top = `${-scrollY}px`;
}

// Function to enable the scrolling
function enableScrolling() {
    const scrollY = parseInt(document.body.style.top);
    document.body.style.position = "";
    document.body.style.top = "";
    window.scrollTo(0, -scrollY); // Scroll back down to where screen was at
}

// Flip benefit based on mouse position
function toggleFlip(card) {
    card.classList.toggle('flipped');
}

const benefitCards = document.querySelectorAll('.benefit');
benefitCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
            toggleFlip(card);
    });
    card.addEventListener('mouseleave', () => {
            toggleFlip(card);
    });
});

let prevScrollPos = window.pageYOffset; // Previous scroll position

// Function to hide/show the header on scroll
window.onscroll = function() {
    const currentScrollPos = window.pageYOffset;
    const navElement = document.getElementById("mainHeader");
    const viewportWidth = window.innerWidth;
    if ((viewportWidth*.5)>300){
        width = 300;
    }
    else{
        width = viewportWidth*.5;
    }

    // Check if scrolled more than width amount of pixels
    if (currentScrollPos > width) {
        if (prevScrollPos > currentScrollPos) {
            document.getElementById("mainHeader").style.top = "0";
        } else {
            document.getElementById("mainHeader").style.top = `-${navElement.clientHeight}px`; // Hide header
        }
    }

    // Keep header visible for the first few hundred pixels
    else {
        document.getElementById("mainHeader").style.top = "0";
    }

    prevScrollPos = currentScrollPos;
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
    const navElement = document.getElementById("mainHeader"); // Check if scroll position is at the top of the page (scrollY is zero)
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
function showJoin() {
    const joinAnswer = document.getElementById("join-answer");
    const joinQuestion = document.getElementById('join-question');
    joinQuestion.classList.add("active");
    joinAnswer.style.display = 'block';
    joinAnswer.style.opacity = '1';
}

// Function to show that the message sent or failed
function showSent(message) {
    console.log(message);
    const send = document.getElementById(message);
    send.style.display = 'block';
}

// Function to show the loading screen
function showLoading() {
    document.getElementById('loading').style.display = 'block';
}