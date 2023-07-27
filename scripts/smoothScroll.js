
let html = document.documentElement;
let body = document.body;
var scrollAnimFrame = null;
var scroller = {
  target: document.querySelector("#scroll-container"),
  ease: 0.05, // <= scroll speed
  y: 0,
  resizeRequest: 1,
  scrollRequest: 0,
};

let prevScroll = 0;
let deltaScroll = 0;


window.addEventListener("load", onLoad);

function onLoad() {    
  updateScroller();  
  window.focus();
  window.addEventListener("resize", onResize);
  document.addEventListener("scroll", onScroll); 
}

function updateScroller() {
  
  var resized = scroller.resizeRequest > 0;
    
  if (resized) {    
    var height = scroller.target.clientHeight;
    body.style.height = height + "px";
    scroller.resizeRequest = 0;
  }
      
  var scrollY = window.scrollY || html.scrollTop || body.scrollTop || 0;
  deltaScroll = (scrollY - scroller.y) * scroller.ease;
  scroller.y += deltaScroll;

  if (Math.abs(scrollY - scroller.y) < 0.05 || resized) {
    scroller.y = scrollY;
    scroller.scrollRequest = 0;
  }
  
  TweenLite.set(scroller.target, { 
    y: -scroller.y 
  });
  scrollAnimFrame = scroller.scrollRequest > 0 ? requestAnimationFrame(updateScroller) : null;
}

function onScroll() {
  scroller.scrollRequest++;
  if (!scrollAnimFrame) {
    scrollAnimFrame = requestAnimationFrame(updateScroller);
  }
}

function onResize() {
  scroller.resizeRequest++;
  if (!scrollAnimFrame) {
    scrollAnimFrame = requestAnimationFrame(updateScroller);
  }
}