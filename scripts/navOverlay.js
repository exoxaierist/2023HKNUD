let buttons = document.querySelectorAll(".navOverlayBtn");
let targetPos = []
let offsets = [[0,0],[0,0],[0,0],[0,0]]
let pGroups = document.querySelectorAll(".pGroup");
let arrowLines = document.querySelectorAll(".arrowLine");
let arrowTargets = document.querySelectorAll(".arrowTarget");

window.onload = Refresh;
window.onresize = ()=>{setTimeout(Refresh,400);}

function Refresh(){
    console.log("refresh");
    const start = document.querySelector(".arrowLine").getBoundingClientRect();
    for (let i = 0; i < buttons.length; i++) {
        const button = arrowTargets[i].getBoundingClientRect();
        targetPos.push([button.left, button.top])
        pGroups[i].style.left = targetPos[i][0]+offsets[i][0]+"px";
        pGroups[i].style.top = targetPos[i][1]+offsets[i][1]+"px";

        arrowLines[i].style.width = Math.sqrt(
            Math.pow(targetPos[i][1]+offsets[i][1]-start.top,2)+
            Math.pow(targetPos[i][0]+offsets[i][0]-start.left,2))+"px";

        var rot = Math.atan2(
            targetPos[i][1]+offsets[i][1]-start.top-1,
            targetPos[i][0]+offsets[i][0]-start.left
            );
        arrowLines[i].style.rotate = rot+"rad";
        
        pGroups[i].style.rotate = rot+Math.PI*1.25 + "rad";
    }
}