window.onload = function mostrarMas() {
  var slice = function(elements, start, end) {
    var sliced = Array.prototype.slice.call(elements, start, end);
    return sliced;
  }
  var filmsToHidde = slice(document.getElementsByClassName('col-md-4'), 6);
  for(var i=0; i<filmsToHidde.length; i++) {
    filmsToHidde[i].style.display = 'none';
  }
  var button = document.getElementsByTagName('button')[0];
  button.onclick = function (){
    for(var i=0; i<filmsToHidde.length; i++) {
      filmsToHidde[i].style.display = 'block';
    }
    button.style.display = 'none';
  }
}
