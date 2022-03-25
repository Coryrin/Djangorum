window.addEventListener('mouseup', e => {
    // Check if something is selected
    // If nothing is selected, it returns true. Otherwise, if something is selected, it's false.
    // Weird.
    if (!getSelection().isCollapsed) {
        const text = getSelection().toString();
        const quoteBtn = document.querySelector('.quote-btn');
        const commentBox = document.querySelector('.comment-field');

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

const loginToggle = document.querySelector('.log-in-label');
const signUpToggle = document.querySelector('.sign-up-label');

if (loginToggle) {
    loginToggle.addEventListener('click', showLoginForm);
}

if (signUpToggle) {
    signUpToggle.addEventListener('click', showSignUpForm);
}

const signUpForm = document.querySelector('.sign-up-form');
const loginForm = document.querySelector('.login-form');

function showLoginForm() {
    signUpForm.style.display = 'none';
    loginForm.style.display = 'block';
}

function showSignUpForm() {
    loginForm.style.display = 'none';
    signUpForm.style.display = 'block';
}

const year = new Date().getFullYear();
document.querySelector('#currentYear').innerText = year;
