function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: "smooth" // Enables smooth scrolling
    });
}


document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    // its like this :

    {/* 

    <a href="#section1">Go to Section 1</a>
    <a href="#section2">Go to Section 2</a>
    <a href="#top">Go to Top</a>

    <div id="section1">Content of Section 1</div>
    <div id="section2">Content of Section 2</div> 
    
    */}





    anchor.addEventListener("click", function(event) {
        event.preventDefault();
        const targetId = this.getAttribute("href").substring(1);
        const targetElement = document.getElementById(targetId);

        if (targetId === "top") {
            // Scroll to the top of the page
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        } else {
            // Scroll to the specific element if it exists
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: "smooth"
                });
            }
        }
    });
});
