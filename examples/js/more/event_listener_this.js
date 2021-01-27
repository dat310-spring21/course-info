function init(){
    document.getElementById("red").onclick = function(){ handleThisGreen()};
}

function handle(element, value){
    if (element.style){
    element.style.backgroundColor = value;
    }
    else {
        console.log("this element has no style");
    }

}

function handleThisGreen(){
    handle(this, "green");
}


window.onload = init;