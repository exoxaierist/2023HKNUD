
let html = document.documentElement;
let body = document.body;
let viewport = document.querySelector(".viewport");
var scrollAnimFrame = null;
let scroller = {
  target: document.querySelector("#scroll-container"),
  ease: 4, // <= scroll speed
  y: 0,
  resizeRequest: 1,
  scrollRequest: 0,
  initial: 1,
};

let prevScroll = 0;
let deltaScroll = 0;
let unscaledDeltaScroll = 0;
let prevTimeStamp,deltaTime;
var OnScroll = function(){};


window.addEventListener("load", onLoad);

function onLoad() {
  viewport.style.overflowY = "hidden";
  
  window.addEventListener("resize", onResize);
  window.focus();
  updateScroller();  
  scroller.resizeRequest = 1;
  setTimeout(()=>scroller.resizeRequest = 1,100);
}

function updateScroller(timeStamp) {
  
  timeStamp = Date.now();
  if(prevTimeStamp == undefined){
    prevTimeStamp = timeStamp;
  }
  deltaTime = (timeStamp - prevTimeStamp)*0.001;
  prevTimeStamp = timeStamp;

  
  var resized = scroller.resizeRequest > 0;
  
  if (resized) {    
    var height = scroller.target.clientHeight;
    body.style.height = height + "px";
    scroller.resizeRequest--;
  }
  
  var scrollY = window.scrollY || html.scrollTop || body.scrollTop || 0;
  unscaledDeltaScroll = (scrollY - scroller.y) * scroller.ease;
  deltaScroll = unscaledDeltaScroll * deltaTime;
  if(document.hasFocus()){
    scroller.y += deltaScroll;
  }else{
    scroller.y = scrollY;
  }
  
  if(scroller.initial > 0) {
    html.scrollTop = viewport.scrollTop; 
    viewport.scrollTop = 0;
    scroller.initial = 0;
  }
  
  if (Math.abs(scrollY - scroller.y) < 0.05 || resized) {
    scroller.y = scrollY;
    scroller.scrollRequest = 0;
  }
  scroller.target.style.transform = "translateY("+-scroller.y+"px)";
  
  OnScroll();
  
  requestAnimationFrame(updateScroller);
}

function onResize() {
  scroller.resizeRequest++;
}
