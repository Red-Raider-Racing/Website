document.addEventListener("DOMContentLoaded", function() {
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

    // Observe all elements with the class "box"
    const boxes = document.querySelectorAll(".box");
    boxes.forEach(function(box) {
    observer.observe(box);
    });
});


// Function to update the padding of the "main" element based on the height of the "nav" element
function updateMainPadding() {
    const logo = document.querySelector(".logo-image")
    const logoCon = document.querySelector(".logo")
    const navMain = document.querySelector(".navMain")
    const altNav = document.querySelector(".altNav")

    const viewportWidth = window.innerWidth;
    if (viewportWidth <= 890 && viewportWidth > 810){
        logo.style.width = '40px';
        navMain.style.display = 'flex';
        altNav.style.display = 'none';
        logoCon.style.padding = '0px'
    }
    else if(viewportWidth <= 810 ){
        logo.style.width = '40px';
        logoCon.style.padding = '0px'
        navMain.style.display = 'none';
        altNav.style.display = 'flex';
    }
    else{
        logo.style.width = '100px';
        navMain.style.display = 'flex';
        altNav.style.display = 'none';
        logoCon.style.padding = '10px'
    }

    const navElement = document.getElementById("mainHeader");
    const mainElement = document.querySelector(".main");
    mainElement.style.paddingTop = `${navElement.clientHeight}px`;
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
    const menuButton = document.querySelector(".menuButton");
    const header = document.getElementById("mainHeader");
    const logo = document.querySelector(".logo-image");

    if (menu.style.display === "block") {
        // Close the menu
        menu.style.display = "none";
        menuButton.innerHTML = "Menu";
        menuButton.style.marginLeft = "0px";
        menuButton.style.marginRight = "0px";
        menuButton.style.marginTop = "0px";
        header.style.height = "";
        logo.style.width = '40px';

        // Enable scrolling
        enableScrolling();
    } else {
        // Open the menu
        menu.style.display = "block";
        menuButton.innerHTML = "&#x2715";
        menuButton.style.marginLeft = "-10px";
        menuButton.style.marginRight = "50px";
        menuButton.style.marginTop = "-120px";
        header.style.height = "100%";
        logo.style.width = '100px';

        // Disable scrolling
        disableScrolling();
    }
}

// Function to disable scrolling
function disableScrolling() {
    const scrollY = window.scrollY;
    document.body.style.position = "fixed";
    document.body.style.top = `-${scrollY}px`;
}

// Function to enable scrolling
function enableScrolling() {
    const scrollY = parseInt(document.body.style.top);
    document.body.style.position = "";
    document.body.style.top = "";
    window.scrollTo(0, scrollY);
}

function toggleFlip(card) {
    card.classList.toggle('flipped');
}

