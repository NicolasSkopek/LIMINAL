function mostrarErro() {
  var audio = document.getElementById('click');
  audio.play();


  var overlay = document.getElementById('overlay');
  overlay.style.display = 'block';


  var erroOverlay = document.getElementById('erroOverlay');
  erroOverlay.style.display = 'block';
}

function fecharErro() {
  var audio = document.getElementById('click');
  audio.play();


  var overlay = document.getElementById('overlay');
  overlay.style.display = 'none';


  var erroOverlay = document.getElementById('erroOverlay');
  erroOverlay.style.display = 'none';
}