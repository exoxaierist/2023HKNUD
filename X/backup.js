let rawDelta = 0;
let normalizedDelta = 0;
let prevNormalizedDelta = 0;
let finalValue = 0;
let prevTransY;
let prevTimeStamp,deltaTime;
let body = document.querySelector("body");
let iframe = document.querySelector("iframe");
let amf;



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

window.onbeforeunload = function(){
    cancelAnimationFrame(amf);
    if(isNaN(parseFloat(finalValue)))localStorage.setItem("prevTransY",0);
    else localStorage.setItem("prevTransY",finalValue.toString());
}
window.onload = function(){
    finalValue = parseFloat(localStorage.getItem("prevTransY"));
    //body.style.transform = prevTransY;
    console.log("onload")
    if(body.classList.contains("hideOverflow")){
        body.style.overflow = "hidden";
    }
    Update(0);
}

function Update(timeStamp){
    if(prevTimeStamp == undefined){
        prevTimeStamp = timeStamp;
    }
    deltaTime = (timeStamp - prevTimeStamp)*0.001;
    prevTimeStamp = timeStamp;
    // smooth scroll
    if(Math.abs(rawDelta) < Math.abs(normalizedDelta)) normalizedDelta += (0-normalizedDelta)*deltaTime*3;
    normalizedDelta = normalizedDelta + (rawDelta-normalizedDelta)*deltaTime*2;
    finalValue += normalizedDelta;
    if(finalValue < 0) finalValue += 0-finalValue*15*deltaTime;
    else if(finalValue > body.clientHeight-window.innerHeight) finalValue = finalValue + (body.clientHeight-window.innerHeight-finalValue)*20*deltaTime;
    body.style.transform = "translateY(" + -finalValue + "px)"
    prevTransY = body.style.transform;
    rawDelta = 0;
    prevNormalizedDelta = normalizedDelta;
    
    dragHistory[0] += (normalizedDelta*2-dragHistory[0]);
    dragHistory[1] += (normalizedDelta*1.8-dragHistory[1]);
    dragHistory[2] += (normalizedDelta*-.1-dragHistory[2]);
    dragHistory[3] += (normalizedDelta*1-dragHistory[3]);
    
    // item juice
    if(smoothItems.length == 0) return;
    for (let i = 0; i < smoothItems.length; i++) {
        const element = smoothItems[i];
        const col = i%4;
        const row=[0,3,2,1];
        element.style.transform = "translateY(" + -dragHistory[row[col]] + "px)"
    }
    amf = requestAnimationFrame(Update);
}