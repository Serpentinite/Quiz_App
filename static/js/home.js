'use strict';
document.getElementById("p2").style.visibility ="hidden";

function clickBtn2(){
	const p2 = document.getElementById("p2");

	if(p2.style.visibility=="visible"){
	    // hiddenで非表示
	    p2.style.visibility ="hidden";
    }else{
	    // visibleで表示
	    p2.style.visibility ="visible";
    }
}
