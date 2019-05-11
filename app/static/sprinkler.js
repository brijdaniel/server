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
	$.get('sprinkler/' + window.opp).done(function(response){
		// change button and status
		setelems(response.status, response.opposite);
	})
}

window.socket.on('statechange', function statechange(change){
	setelems(change.status, change.opposite);
})