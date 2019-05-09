function action(action){
	$.get('sprinkler/' + action).done(function(response){
		// want to repeat the jinja2 if statement span id=if
		// not sure how to do this
	}).fail(function(){
		// error sprinkler not respond
	})
}