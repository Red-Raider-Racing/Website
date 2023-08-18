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
    const navElement = document.querySelector("nav");
    const mainElement = document.querySelector(".main");
    mainElement.style.paddingTop = `${navElement.clientHeight}px`;
}

// Initial update when the DOM is ready
document.addEventListener("DOMContentLoaded", updateMainPadding);

// Update padding on window resize
window.addEventListener("resize", updateMainPadding);
