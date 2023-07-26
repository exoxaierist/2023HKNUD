let activeFilter = [];
let allBtn = document.querySelector(".allBtn");
let items = $(".itemContainer");
let animating = false;
let fadeTime = 150;

$(".filterBtn").click(function(){
    if(animating) return;
    let filter = $(this).attr("filter");
    if(activeFilter.length==0) HideAllItems();
    else FilterHideItems();
    $(allBtn).removeClass("clicked");
    $(this).toggleClass("clicked");
    if(activeFilter.includes("."+filter)) activeFilter.splice(activeFilter.indexOf("."+filter),1);
    else activeFilter.push("."+filter);

    if(activeFilter.length==0){
        $(allBtn).addClass("clicked");
        setTimeout(ShowAllItems,fadeTime-15);
        setTimeout(()=>animating=false,fadeTime*2);
    }else{
        setTimeout(FilterShowItems,fadeTime-15);
        setTimeout(()=>animating=false,fadeTime*2);
    }
})

$(allBtn).click(SelectAll)

SelectAll();

function SelectAll(){
    if(animating) return;
    FilterHideItems();
    activeFilter = [];
    $(".filterBtn").removeClass("clicked");
    $(allBtn).addClass("clicked");
    setTimeout(ShowAllItems,fadeTime-15);
    setTimeout(()=>animating=false,fadeTime*2);
}
function FilterHideItems(){
    animating = true;
    items.filter(activeFilter.join(", ")).fadeOut(fadeTime);
}
function FilterShowItems(){
    items.filter(activeFilter.join(", ")).fadeIn(fadeTime);
}
function HideAllItems(){
    animating = true;
    items.fadeOut(fadeTime);
}
function ShowAllItems(){
    items.fadeIn(fadeTime);
}
