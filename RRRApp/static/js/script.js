document.addEventListener("DOMContentLoaded", function() {
    const questions = document.querySelectorAll(".faq");
    
    questions.forEach(question => {
      question.addEventListener("click", function() {
        const answer = this.nextElementSibling;
        
        if (answer.style.display === "block") {
          answer.style.opacity = 0;
          setTimeout(() => {
            answer.style.display = "none";
          }, 20);
        } else {
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
          
          this.classList.add("active");
          
          answer.style.display = "block";
          setTimeout(() => {
            answer.style.opacity = 1;
          }, 10);
        }
      });
    });
    // Function to check if an element is intersecting the viewport
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

    const members = document.querySelectorAll(".member");
    members.forEach(function(member) {
    observer.observe(member);
    });

    const benefits = document.querySelectorAll(".benefit");
    benefits.forEach(function(benefit) {
    observer.observe(benefit);
    });

    const cars = document.querySelectorAll(".car");
    cars.forEach(function(car) {
    observer.observe(car);
    });

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

    if (menu.style.display === "block") {
        // Close the menu
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

// Add an event listener to the document that listens for clicks
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

        // Enable scrolling
        enableScrolling();
    } else {
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

        // Disable scrolling
        disableScrolling();
    }
}

// Function to disable scrolling
function disableScrolling() {
    const scrollY = window.scrollY;
    document.body.style.position = "fixed";
    document.body.style.top = `${-scrollY}px`;
}

// Function to enable scrolling
function enableScrolling() {
    const scrollY = parseInt(document.body.style.top);
    document.body.style.position = "";
    document.body.style.top = "";
    window.scrollTo(0, -scrollY);
}

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

let prevScrollPos = window.pageYOffset;

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

    if (currentScrollPos > width) { // Check if scrolled more than 100 pixels
        if (prevScrollPos > currentScrollPos) {
            document.getElementById("mainHeader").style.top = "0";
        } else {
            document.getElementById("mainHeader").style.top = `-${navElement.clientHeight}px`; // Hide header
        }
    } else {
        document.getElementById("mainHeader").style.top = "0"; // Keep header visible for the first 100 pixels
    }

    prevScrollPos = currentScrollPos;
};

window.addEventListener('scroll', function () {
    const scrollY = window.scrollY;
    const parallaxBackground = document.querySelector('.coverIMG');
    const pageTitle = document.querySelector('.pageTitle');

    if (parallaxBackground != null){
        parallaxBackground.style.transform = `translateY(${scrollY * 0.5}px)`;
    }
    
    pageTitle.style.transform = `translateY(-${scrollY * .2}px)`;
});

window.addEventListener('scroll', function () {
    const scrollY = window.scrollY;
    const navElement = document.getElementById("mainHeader");

    // Check if scroll position is at the top of the page (scrollY is zero)
    if (scrollY === 0 && document.body.style.top >= 0) {
        // Scroll is at the top, make the header clear and remove box shadow
        navElement.style.backgroundColor = "transparent";
        navElement.style.boxShadow = "none";
    } else {
        // Scroll is not at the top, set background color and box shadow as needed
        navElement.style.backgroundColor = "var(--primary-faded-color)"; // Replace with your desired color
        navElement.style.boxShadow = "var(--shadow)"; // Replace with your desired shadow
    }

    // Rest of your scroll event handling code...
});