let locators = document.querySelectorAll(".locator");
let paths = document.querySelectorAll(".path");
let mousePos = { x: undefined, y: undefined };

window.addEventListener('mousemove', (event) => {
    mousePos = { x: event.clientX, y: event.clientY };
  });

Update();
function Update(){
    var closest = 100000000;
    var closestLocator = 0;
    for (let i = 0; i < locators.length; i++) {
        var locator = locators[i].getBoundingClientRect();
        var length = Math.pow(Math.abs(locator.x-mousePos.x),2) + Math.pow(Math.abs(locator.y-mousePos.y),2)
        if(length<closest){
            closest = length
            closestLocator = i;
        }
    }
    for (let i = 0; i < locators.length; i++) {
        paths[i].style.strokeWidth = "0px";
    }
    paths[closestLocator].style.strokeWidth = "40px";

    console.log(mousePos)

    requestAnimationFrame(Update);
}