let rawDelta = 0;
let normalizedDelta = 0;
let prevNormalizedDelta = 0;
let finalValue = 0;
let prevTimeStamp,deltaTime;
let body = document.querySelector("body");
let iframe = document.querySelector("iframe");

if(body.classList.contains("hideOverflow")){
    body.style.overflow = "hidden";
}

let smoothItems = document.querySelectorAll(".itemContainer");
let drag = 0;
let dragHistory = [0,0,0,0];

window.addEventListener("wheel", function(e){
    rawDelta = e.deltaY;
})
if(iframe != undefined){
    iframe.addEventListener("wheel", function(e){
        rawDelta = e.deltaY;
    })
}


Update();
function Update(timeStamp){
    requestAnimationFrame(Update);
    if(prevTimeStamp == undefined){
        prevTimeStamp = timeStamp;
    }
    deltaTime = (timeStamp - prevTimeStamp)*0.001;
    prevTimeStamp = timeStamp;
    // smooth scroll
    normalizedDelta = normalizedDelta + (rawDelta-normalizedDelta)*0.03;
    finalValue += normalizedDelta;
    if(finalValue < 0) finalValue += 0-finalValue*15*deltaTime;
    else if(finalValue > body.clientHeight-window.innerHeight) finalValue = finalValue + (body.clientHeight-window.innerHeight-finalValue)*20*deltaTime;
    body.style.transform = "translateY(" + -finalValue + "px)"
    rawDelta = 0;
    prevNormalizedDelta = normalizedDelta;

    dragHistory[0] += (normalizedDelta*1-dragHistory[0])*1;
    dragHistory[1] += (normalizedDelta*3-dragHistory[1])*0.8;
    dragHistory[2] += (normalizedDelta*2-dragHistory[2])*0.7;
    dragHistory[3] += (normalizedDelta*4-dragHistory[3])*0.4;

    // item juice
    if(smoothItems.length == 0) return;
    for (let i = 0; i < smoothItems.length; i++) {
        const element = smoothItems[i];
        const col = i%4;
        const row=[0,3,1,2];
        element.style.transform = "translateY(" + -dragHistory[row[col]] + "px)"
    }
}