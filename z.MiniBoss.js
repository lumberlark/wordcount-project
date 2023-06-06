document.getElementById("button1").onclick = function(){
    document.getElementById("video").innerHTML = "<h3><strong>Place-Holder for now</strong></h3>";
    document.getElementById("video").style = "color:Orange";
}

document.getElementById("reset").onclick = function() {
    document.getElementById("video").innerHTML = "<h4><Strong>Video will be placed here</strong></h4>";
    document.getElementById("video").style = "color:white";
}

function swap(id1,id2,id3){
    var s =document.getElementById(id1).innerHTML;
    var d =document.getElementById(id2).innerHTML;
    var k =document.getElementById(id3).innerHTML;
}