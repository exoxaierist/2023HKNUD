let dragItems = document.querySelectorAll(".itemContainer");
let rand = 150;
let refresh = true;

Update();

function Update(){
    if(refresh && Math.abs(deltaScroll)<0.3) {rand = Math.round(Math.random() *1000); refresh = false;console.log(rand);}
    if(Math.abs(deltaScroll) > 10) refresh = true;

    for (let i = 0; i < dragItems.length; i++) {
        const element = dragItems[i];
        let top = element.getBoundingClientRect().top / window.innerHeight;
        left = (((i*rand*i*rand)*0.1)%1)*10-5
        top = deltaScroll>0?-(1-top):-top;
        
        element.style.transform = "translateY(" + ((deltaScroll*top*10)+0.35*left*deltaScroll) + "px)"
    }
    requestAnimationFrame(Update);
}
