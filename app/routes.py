import os
from time import sleep
from flask import render_template, flash, redirect, url_for, request
from app import app, mqtt, redis, convert, monitor, socketio
from app.forms import SpScheduleForm, SpTimer
from flask_breadcrumbs import register_breadcrumb
from flask_socketio import emit

@app.route('/')
@app.route('/index')
@register_breadcrumb(app, '.', 'Home')
def index():
    return render_template('index.html')

@app.route('/sprinkler')
@register_breadcrumb(app, '.sprinkler', 'Sprinkler')
def sprinkler():

	status = convert.switch(redis.db.get('pihouse/sprinkler/status'))
	opposite = convert.convert(status)

	mqtt.client.publish('pihouse/sprinkler/schedule/last', "request")
	mqtt.client.publish('pihouse/sprinkler/schedule/next', "request")

	sleep(0.15)
	
	last_run = redis.db.get('pihouse/sprinkler/schedule/last')
	next_run = redis.db.get('pihouse/sprinkler/schedule/next')
	
	templateData = {
		'status' : status,
		'opposite' : opposite,
		'last_run' : last_run,
		'next_run' : next_run
	}
	
	return render_template('sprinkler.html', **templateData)

@app.route('/sprinkler/<action>')
def action(action):
	if action == 'on':
		if not redis.db.get('pihouse/sprinkler/status') == "True":
			mqtt.client.publish('pihouse/sprinkler/control', "True")
			monitor.run()

	if action == 'off':
		mqtt.client.publish('pihouse/sprinkler/control', "False")
		mqtt.client.publish('pihouse/sprinkler/schedule/last', "request")

	sleep(0.2)
	status = redis.db.get('pihouse/sprinkler/status')
	socketio.emit('statechange', {"status": convert.switch(status), "opposite": convert.convert(status)})
	return ('', 204)

@app.route('/sprinkler/timer', methods=['GET','POST'])
@register_breadcrumb(app, '.sprinkler.timer', 'Timer')
def sp_timer():
	form = SpTimer(timer=float(redis.db.get('pihouse/sprinkler/timer')))

	if request.method == 'GET' or not form.validate_on_submit():
		if not isinstance(redis.db.get('pihouse/sprinkler/timer'), int): 
			mqtt.client.publish('pihouse/sprinkler/timer', "request")
			sleep(0.1)
		if not str(redis.db.get('pihouse/sprinkler/timer')) == "request":
			flash('Timer is currently %s mins' %float(redis.db.get('pihouse/sprinkler/timer')))

	elif request.method == 'POST' and form.validate_on_submit():
		flash('Timer set to %s mins' %form.timer.data)
		mqtt.client.publish('pihouse/sprinkler/timer', float(form.timer.data))

	return render_template('sp_timer.html', title='Sprinkler Timer',form=form)

@app.route('/sprinkler/schedule', methods=['GET', 'POST'])
@register_breadcrumb(app, '.sprinkler.schedule', 'Schedule')
def sp_schedule():
	schedule = redis.db.get('pihouse/sprinkler/schedule').split()
	form = SpScheduleForm(minute=schedule[0], hour=schedule[1], dom=schedule[2], month=schedule[3], dow=schedule[4])
	
	if request.method == 'GET' or not form.validate_on_submit():
		if not isinstance(redis.db.get('pihouse/sprinkler/schedule'), str): # or list?
			mqtt.client.publish('pihouse/sprinkler/schedule', "request")
			sleep(0.1)

	elif request.method == 'POST' and form.validate_on_submit():
		schedule = '%s %s %s %s %s' %(str(form.minute.data), str(form.hour.data), str(form.dom.data), str(form.month.data), str(form.dow.data))
		mqtt.client.publish('pihouse/sprinkler/schedule', str(schedule))
		mqtt.client.publish('pihouse/sprinkler/schedule/set', str(form.use_schedule.data))
		flash('Schedule set!')

	return render_template('sp_schedule.html', title='Sprinkler Schedule',form=form)

"""
@app.route('/sprinkler/log')

"""