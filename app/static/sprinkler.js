function status(status='False'){
	// convert status to on/off
	if (status = 'True') {
		document.getElementById("status").innerHTML = 'on';
		document.getElementById("opposite").innerHTML = 'off';
		console.log('status = true')
	} else {
		document.getElementById("status").innerHTML = 'off';
		document.getElementById("opposite").innerHTML = 'on';
		console.log('status = false')
	}
}

function action(action){
	$.get('sprinkler/' + action).done(function(response){
		// change button and status
		status(response)
	})
}