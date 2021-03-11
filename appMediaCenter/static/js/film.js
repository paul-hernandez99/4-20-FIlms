
window.onload = function changeVideoBackground() {
  var video = document.getElementsByTagName("video")[0];
  video.poster = "/static/media/transparent/transparent.png";
  video.style.backgroundImage = "url("+film_url_img+")";
  video.style.backgroundSize = "cover";
  video.addEventListener("play", blackBackground);
  function blackBackground() {
  video.style.background = "black";
  }
}
