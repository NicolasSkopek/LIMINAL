function playSound(filename) {
    var audio = document.getElementById(filename);
    audio.play();
}

document.addEventListener('DOMContentLoaded', function () {
    var modals = document.querySelectorAll('.modal');

    modals.forEach(function (modal) {
        modal.addEventListener('click', function (event) {
            if (event.target === modal) {
                playSound("pop-up-blocked");
            }
        });
    });
});
