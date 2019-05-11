function setelems(status, opposite){
	// set html elems
	document.getElementById("status").innerHTML = status;
	document.getElementById("opposite").innerHTML = opposite;
	window.opp=opposite;
	if (status == 'on'){
		document.getElementById("button").className = ("btn btn-block btn-lg btn-default")
	} else {
		document.getElementById("button").className = ("btn btn-block btn-lg btn-primary")
	}
}

function action(){
	act=window.opp;
	$.get('sprinkler/' + act).done(function(response){
		// change button and status
		setelems(response.status, response.opposite);
	})
}