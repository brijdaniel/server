function setelems(status, opposite){
	// set html elems
	document.getElementById("status").innerHTML = status;
	document.getElementById("opposite").innerHTML = opposite;
	window.opp=opposite;
	if (status == 'on'){
		document.getElementById("button").className = ("btn btn-block btn-lg btn-default");
	} else {
		document.getElementById("button").className = ("btn btn-block btn-lg btn-primary");
	};
};

function action(){
	// send get request with action to server
	$.get('sprinkler/' + window.opp)
};

//  Callback from socket msg 'statechange'
window.socket.on('statechange', function statechange(change){
	setelems(change.status, change.opposite);
});
