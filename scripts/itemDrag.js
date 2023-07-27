let dragItems = document.querySelectorAll(".itemContainer");

Update();

function Update(){

    for (let i = 0; i < dragItems.length; i++) {
        const element = dragItems[i];
        let top = element.getBoundingClientRect().top / window.innerHeight;
        let left = element.getBoundingClientRect().left / window.innerWidth;
        top = deltaScroll>0?top:-top;
        left = Math.ceil(((((left*i)*(left+i*151))*100)%1)*10)*0.15;
        TweenLite.set(element, {
            y: deltaScroll*top*4*left
            });
    }
    requestAnimationFrame(Update);
}