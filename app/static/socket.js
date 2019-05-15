function connectsocket(){
	window.socket = io.connect(); // need to make this accessible to sprinker.js
	console.log("socket connected");
};

$(document).ready(connectsocket())