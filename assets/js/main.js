window.addEventListener('mouseup', e => {
    // Check if something is selected
    // If nothing is selected, it returns true. Otherwise, if something is selected, it's false.
    // Weird.
    if (!getSelection().isCollapsed) {
        text = getSelection().toString();
        
        let quoteBtn = document.querySelector('.quote-btn');
        let commentBox = document.querySelector('.comment-field');

        quoteBtn.style.display = 'block';
        quoteBtn.style.top = e.layerY + 'px';
        quoteBtn.style.left = e.clientX + 'px';

        quoteBtn.addEventListener('mouseup', e => {
            let output = `<em>"${text}"</em>`;
            commentBox.value = output;
            quoteBtn.style.display = 'none';
        });
    };
});

let loginToggle = document.querySelector('.log-in-label');
let signUpToggle = document.querySelector('.sign-up-label');

loginToggle.addEventListener('click', showLoginForm);

signUpToggle.addEventListener('click', showSignUpForm);

let signUpForm = document.querySelector('.sign-up-form');

let loginForm = document.querySelector('.login-form');


function showLoginForm() {
    signUpForm.style.display = 'none';
    loginForm.style.display = 'block';
}

function showSignUpForm() {
    loginForm.style.display = 'none';
    signUpForm.style.display = 'block';
}

