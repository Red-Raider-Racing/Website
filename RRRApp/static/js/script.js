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
    if (viewportWidth <= 758 && viewportWidth > 676){
        logo.style.width = '40px';
        navMain.style.display = 'flex';
        altNav.style.display = 'none';
        logoCon.style.padding = '0px'
    }
    else if(viewportWidth <= 676 ){
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
    const menuButton = document.querySelector(".dropdown");
    const menu = document.querySelector(".dropdown-content");
    if (!menuButton.contains(event.target)) {
        menu.style.display = "none";
    }
});

// Function to toggle the display of the dropdown content
function toggleMenu() {
    const menu = document.querySelector(".dropdown-content");
    if(menu.style.display == "block"){
        menu.style.display = "none";
    }
    else{
        menu.style.display = "block";
    }
}

