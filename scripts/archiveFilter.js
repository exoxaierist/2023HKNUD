let filterList = [["all"],["all"],["all"],["all"]];
let activeFilters = [[],[],[],[]];
let combinedFilter;
let filterAllBtns = document.querySelectorAll(".allBtn");
let filterItems = $(".itemContainer");
let filterTransiting = false;
let filterFadeDuration = 150;
const filterGroupCount = 2;


$(".filterBtn").each(function(i){
    filterList[$(this).attr("filterGroup")].push("." +$(this).attr("filter"));
})

for (let i = 0; i < filterGroupCount; i++) {
    SelectAll(i);
}


$(".filterBtn").click(function(){
    OnClick($(this));
})

$(".allBtn").click(function(){
    SelectAll($(this).attr("filterGroup"));
})

function OnClick(element){
    const group = parseInt($(element).attr("filterGroup"));
    const filter = $(element).attr("filter");

    // remove filter if all flag
    if(activeFilters[group].includes("all")) {
        activeFilters[group] = [];
        $(filterAllBtns[group]).removeClass("clicked");
    }

    // add/remove from activefilters
    if(activeFilters[group].includes("."+filter)){
        activeFilters[group].splice(activeFilters[group].indexOf("."+filter),1);
        $(element).removeClass("clicked");
    }else {
        activeFilters[group].push("."+filter);
        $(element).addClass("clicked");
    }

    // empty or all filter; enable all btn
    if(activeFilters[group].length==0 || activeFilters[group].length == filterList[group].length-1){
        SelectAll(group);
    }else RefreshCombinedFilter();
}

function SelectAll(group){
    activeFilters[group] = filterList[group];
    $(filterAllBtns[group]).addClass("clicked");
    $(".filterBtn").each(function(){
        if($(this).attr("filterGroup") == group) $(this).removeClass("clicked");
    })
    RefreshCombinedFilter();
}

function RefreshCombinedFilter(){
    combinedFilter = "";
    for (let i = 0; i < filterGroupCount; i++) {
        combinedFilter += activeFilters[i].join(", ");
    }
    FilterHideItems();
    setTimeout(FilterShowItems,filterFadeDuration-15);
    setTimeout(()=>filterTransiting=false,filterFadeDuration*2);
}

function FilterHideItems(){
    filterTransiting = true;
    filterItems.fadeOut(filterFadeDuration);
}
function FilterShowItems(){
    var temp = $(filterItems);
    for (let i = 0; i < filterGroupCount; i++) {
        temp = temp.filter(activeFilters[i].join(", "))
    }
    temp.fadeIn(filterFadeDuration);
}
