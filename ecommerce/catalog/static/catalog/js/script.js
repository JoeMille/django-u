console.log("JavaScript is being loaded!");

// Header image pulsating effect

const header = document.querySelector('.site-header');
        let brightness = 1;

        setInterval(() => {
            brightness = brightness === 1 ? 1.5 : 1;
            header.style.filter = `brightness(${brightness})`;
        }, 2000);


