let dragItems = document.querySelectorAll(".itemDrag");
let rand = 150; 
let refresh = true;

OnScroll = UpdateItemDrag;

function UpdateItemDrag(){
    //console.log(deltaTime)
    if(refresh && Math.abs(deltaScroll)<0.3) {rand = Math.round(Math.random() *1000); refresh = false;}
    if(Math.abs(deltaScroll) > 10) refresh = true;
    for (let i = 0; i < dragItems.length; i++) {
        const element = dragItems[i];
        let top = element.getBoundingClientRect().top / window.innerHeight;
        left = (((i*rand*i*rand)*0.1)%1)*10-5
        top = deltaScroll>0?-(1-top):-top;
        element.style.transform = "translateY(" + ((unscaledDeltaScroll*top*3)+0.15*left*unscaledDeltaScroll)*0.001 + "vw)"
    }
}
