// Simple example to handle like, dislike or comment interaction
const likeButtons = document.querySelectorAll('.actions span');

likeButtons.forEach(button => {
    button.addEventListener('click', () => {
        alert('Action clicked!');
    });
});
