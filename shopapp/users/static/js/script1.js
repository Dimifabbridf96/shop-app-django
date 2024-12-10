document.addEventListener("DOMContentLoaded", function() {
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(function(message) {
        setTimeout(function() {
            message.classList.add('fade-out');
            setTimeout(function() {
                message.remove();
            }, 1000); // Adjust the delay time as needed
        }, 5000); // Adjust the display time as needed
    });
});


document.addEventListener('DOMContentLoaded', function() {
    // Get all tab links
    var tabLinks = document.querySelectorAll('.nav-tabs a');

    // Add click event listener to each tab link
    for (var i = 0; i < tabLinks.length; i++) {
        tabLinks[i].addEventListener('click', function(e) {
            e.preventDefault();

            // Get the target tab ID
            var targetTabId = this.getAttribute('href');

            // Remove the 'active' class from all tab links
            for (var j = 0; j < tabLinks.length; j++) {
                tabLinks[j].classList.remove('active');
            }

            // Add the 'active' class to the clicked tab link
            this.classList.add('active');

            // Hide all tab panes
            var tabPanes = document.querySelectorAll('.tab-content .tab-pane');
            for (var k = 0; k < tabPanes.length; k++) {
                tabPanes[k].classList.remove('active');
            }

            // Show the target tab pane
            var targetTabPane = document.querySelector(targetTabId);
            targetTabPane.classList.add('active');
        });
    }
});
