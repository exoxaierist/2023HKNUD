let buttons = document.querySelectorAll(".navOverlayBtn");
let targetPos = [[],[],[],[]]
let offsets = [[0,0],[0,0],[0,0],[0,0]]
let pGroups = document.querySelectorAll(".pGroup");
let arrowLines = document.querySelectorAll(".arrowLine");
let arrowCircles = document.querySelectorAll(".arrowCircle");
let arrowTargets = document.querySelectorAll(".arrowTarget");

//window.onload = Refresh;
//window.onresize = ()=>{Refresh();}
$(buttons).on("mouseenter",Refresh);
$(buttons).on("mouseexit",Clear);

let navOverlay = document.querySelector("#navOverlay");
let navXbtn = document.querySelector(".navXBtn");

let navPageTop = $(".navPageTop");
let navPageBottom = 4(".navPageBottom");

let navMOpen = $(".navMOpen");
let navMClose = $(".navMClose");
let navMCloseArea = $(".navMCloseArea");
let navMContainer = $(".navMContainer");

let overlayState = false;

$(".overlayToggle").on("click",ToggleOverlay)
window.onscroll = ScrollCloseOverlay;
navMOpen.on("click",()=>navMContainer.addClass("navMContainerOpen"));
navMClose.on("click",MScrollCloseOverlay);
navMCloseArea.on("click",MScrollCloseOverlay);

function MScrollCloseOverlay(){
    navMContainer.removeClass("navMContainerOpen");
}
function ScrollCloseOverlay(){
    if(overlayState){
        ToggleOverlay();
    }
    MScrollCloseOverlay();
}

function ToggleOverlay(){
    if(overlayState){
        //close
        navOverlay.style.top = "-30vh";
        overlayState = false;
        navXbtn.style.rotate = "0deg";
        document.querySelector(".navOverlayCancel").style.display = "none";
    }
    else{
        //open
        navOverlay.style.top = "0vh";
        overlayState = true;
        document.querySelector(".navOverlayCancel").style.display = "initial";
    }
}

function Refresh(){
    targetPos = [];
    var i = $(buttons).index($(this));
    var arrowLine = $(arrowLines[i]);
    var startX=(Math.random()*0.6+0.2)*window.innerWidth;
    var startY=(Math.random()*0.5+0.4)*window.innerHeight;
    const target = arrowTargets[i]

    targetPos[i] = [$(target).offset().left,$(target).offset().top-window.scrollY];
    console.log(arrowLine.outerWidth());

    arrowLines[i].style.width = Math.sqrt(
        Math.pow(targetPos[i][1]+offsets[i][1]-startY,2)+
        Math.pow(targetPos[i][0]+offsets[i][0]-startX,2))+"px";
    arrowLines[i].style.left = startX + "px";
    arrowLines[i].style.top = startY + "px";
    arrowCircles[i].style.left = startX + "px";
    arrowCircles[i].style.top = startY + "px";


    var rot = Math.atan2(
        targetPos[i][1]+offsets[i][1]-startY,
        targetPos[i][0]+offsets[i][0]-startX
        );
    arrowLines[i].style.rotate = rot+"rad";
    
    pGroups[i].style.rotate = rot+Math.PI*1.25 + "rad";
}

function Clear(){
    var i = $(buttons).index($(this));
    arrowLines[i].style.width="0px";
}