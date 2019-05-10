function setelems(status, opposite){
	// set html elems
	//[stat, opp] = status(current)
	document.getElementById("status").innerHTML = status;
	document.getElementById("opposite").innerHTML = opposite;
	console.log('status = ' + status);
}

function action(action){
	$.get('sprinkler/' + action).done(function(response){
		// change button and status
		// need to JSON.parse response so I can pass the args to setelems
		setelems(status, opposite);
	})
}