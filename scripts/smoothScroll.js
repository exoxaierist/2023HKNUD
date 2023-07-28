
let html = document.documentElement;
let body = document.body;
var scrollAnimFrame = null;
let scroller = {
  target: document.querySelector("#scroll-container"),
  ease: 5, // <= scroll speed
  y: 0,
  resizeRequest: 1,
  scrollRequest: 0,
};

let prevScroll = 0;
let deltaScroll = 0;
let prevTimeStamp,deltaTime;


window.addEventListener("load", onLoad);

function onLoad() {    
  updateScroller();  
  window.focus();
  window.addEventListener("resize", onResize);
}

function updateScroller(timeStamp) {
  if(prevTimeStamp == undefined){
    prevTimeStamp = timeStamp;
  }
  deltaTime = (timeStamp - prevTimeStamp)*0.001;
  prevTimeStamp = timeStamp;
  
  var resized = scroller.resizeRequest > 0;
    
  if (resized) {    
    var height = scroller.target.clientHeight;
    body.style.height = height + "px";
    scroller.resizeRequest = 0;
  }
      
  var scrollY = window.scrollY || html.scrollTop || body.scrollTop || 0;
  deltaScroll = (scrollY - scroller.y) * scroller.ease * deltaTime;
  scroller.y += deltaScroll;

  if (Math.abs(scrollY - scroller.y) < 0.05 || resized) {
    scroller.y = scrollY;
    scroller.scrollRequest = 0;
  }

  scroller.target.style.transform = "translateY("+-scroller.y+"px)";

  requestAnimationFrame(updateScroller);
}

function onResize() {
  scroller.resizeRequest++;
}
