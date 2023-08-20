 // Function to create a responsive browser window and show a greeting message
 function createResponsiveWindow() {
    // Define the dimensions of the window
    const windowWidth = Math.min(800, window.innerWidth);
    const windowHeight = Math.min(600, window.innerHeight);

    // Open a new browser window with the specified dimensions
    const newWindow = window.open('', '_blank', `width=${windowWidth},height=${windowHeight}`);

    // Write the greeting message to the new window
    newWindow.document.write('<html><head><title>Welcome</title></head><body>');
    newWindow.document.write('<h1>Welcome to Sharif\'s Web App</h1>');
    newWindow.document.write('<p>Welcome to my Flask Webb app. Use it to check the Stock Market and watch videos related to the stocks you find and other related topics. Enjoy!</p>');
    newWindow.document.write('</body></html>');

    // Close the document writing to allow for proper rendering
    newWindow.document.close();
}

// Call the function to create the responsive window and display the greeting
createResponsiveWindow();