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
        let left = element.getBoundingClientRect().left / window.innerWidth;
        left = Math.round(((((left*(i+rand))*(left+i*rand))*100)%1)*10)*0.15;
        top = deltaScroll>0?-(1-top):-top;
        TweenLite.set(element, {
            y: deltaScroll*top*4*left
            });
    }
    requestAnimationFrame(Update);
}