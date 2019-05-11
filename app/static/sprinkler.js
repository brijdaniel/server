function setelems(status, opposite){
	// set html elems
	document.getElementById("status").innerHTML = status;
	document.getElementById("opposite").innerHTML = opposite;
	window.opp=opposite;
	if (status == 'True'){
		document.getElementById("button").className = ("btn btn-block btn-lg btn-default")
	} else {
		document.getElementById("button").className = ("btn btn-block btn-lg btn-primary")
	}
	console.log('status = ' + status);
}

function action(){
	act=window.opp;
	$.get('sprinkler/' + act).done(function(response){
		// change button and status
		console.log(response.status);
		console.log(response.opposite);
		setelems(response.status, response.opposite);
	})
}