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

//  want to abstract this to socket.js and just keep the callback fn here
$(document).ready(function() {
	window.socket = io.connect();
	console.log("socket connected");
	socket.on('statechange', function statechange(change){
		setelems(change.status, change.opposite);
	});
});