
// Header image pulsating effect

const header = document.querySelector('.site-header');
        let brightness = 1;

        setInterval(() => {
            brightness = brightness === 1 ? 1.5 : 1;
            header.style.filter = `brightness(${brightness})`;
        }, 2000);

// Stripe Js payment form 

var stripe = Stripe('pk_test_51J0ZQvK5Q5ZQ5Q5ZQ5');
var elements = Stripe.elements();

var card = elements.create('card');

card.mount('#card-element');

var form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
    event.preventDefault();

    stripe.createtoken(card).then(function(result) {
        if (result.error) {
            var errorElement = document.getElementById('card-errors');
            errorElement.textContent = result.error.message;
        } else {
            stripeTokenHandler(result.token);
        }
    });
});

// Submit Stripe form to Django

function stripeTokenHandler(token) {
    var form = document.getElementById('payment-form');
    var hiddenInput = document.createElement('input');
    hiddenInput.setAttribute('type', 'hidden');
    hiddenInput.setAttribute('name', 'stripeToken');
    hiddenInput.setAttribute('value', 'token.id');
    form.appendChild(hiddenInput);

    form.onsubmit();
}

console.log("JavaScript is being loaded!");