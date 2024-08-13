$(document).ready(function() {
    const headerText = "¡Bienvenido a Honey Coffee!";
    const $headerElement = $('.welcome-message h1');
    let headerIndex = 0;

    function typeWriterHeader() {
        if (headerIndex < headerText.length) {
            $headerElement.append(headerText.charAt(headerIndex));
            headerIndex++;
            setTimeout(typeWriterHeader, 100); // Adjust speed here
        }
    }

    typeWriterHeader(); // Start typing the header text

    // Rotation logic
    function rotateImage() {
        var $backgroundImage = $('.background-image');
        var isForward = true;

        function startRotation() {
            var animationName = isForward ? 'rotateForward' : 'rotateBackward';
            $backgroundImage.css('animation', `${animationName} 10s ease-in-out forwards`);
            
            // Toggle rotation direction for the next iteration
            isForward = !isForward;

            // Pause after animation ends
            setTimeout(function() {
                $backgroundImage.css('animation', 'none'); // Stop the animation
                setTimeout(startRotation, 1000); // Pause duration (1 second)
            }, 10000); // Animation duration (10 seconds)
        }

        startRotation(); // Initialize rotation
    }

    rotateImage(); // Start the rotation effect
});
