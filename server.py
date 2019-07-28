from app import app, socketio

if __name__ == "__main__":
	socketio.run(app, host='10.1.1.3', port=80, debug=False, max_size=3000)
