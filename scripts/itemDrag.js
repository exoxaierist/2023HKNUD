let dragItems = document.querySelectorAll(".itemDrag");
let rand = 150; 
let refresh = true;
let lefts =[];

OnScroll = UpdateItemDrag;

for (let i = 0; i < dragItems.length; i++) {
    lefts.push(Math.random()*10 - 5);
}

function UpdateItemDrag(){
    if(refresh && Math.abs(deltaScroll)<0.3) {rand = Math.round(Math.random() *1000); refresh = false;}
    if(Math.abs(deltaScroll) > 10) refresh = true;
    for (let i = 0; i < dragItems.length; i++) {
        const element = dragItems[i];
        let top = element.getBoundingClientRect().top / window.innerHeight;
        top = deltaScroll>0?-(1-top):-top;
        element.style.transform = "translateY(" + ((unscaledDeltaScroll*top*3)+0.15*((lefts[i]+5+rand)%10-5)*unscaledDeltaScroll)*0.001 + "rem)"
    }
}
