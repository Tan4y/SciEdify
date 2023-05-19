alert('ddd');


function pullDown(arrow) {
    console.log("Neshto");
    //const paragraph = document.getElementById(id);
    const arr = document.getElementById(arrow);
    if (arr.classList.contains("fa-angle-down")) {
      //paragraph.style.height = paragraph.firstElementChild.offsetHeight + "px";
      arr.classList.remove("fa-angle-down");
      arr.classList.add("fa-angle-up");
    }
    else{
        //paragraph.style.height = "149px
        arr.classList.remove("fa-angle-up");
        arr.classList.add("fa-angle-down");
    }
}