import os
from time import sleep
from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, mqtt, redis
from app.forms import SpScheduleForm, SpTimer
from flask_breadcrumbs import register_breadcrumb

@app.route('/')
@app.route('/index')
@register_breadcrumb(app, '.', 'Home')
def index():
    return render_template('index.html')

@app.route('/sprinkler')
@register_breadcrumb(app, '.sprinkler', 'Sprinkler')
def sprinkler():

	status = redis.db.get('pihouse/sprinkler/status')

	mqtt.client.publish('pihouse/sprinkler/schedule/last', "request")
	mqtt.client.publish('pihouse/sprinkler/schedule/next', "request")

	sleep(0.15)
	
	last_run = redis.db.get('pihouse/sprinkler/schedule/last')
	next_run = redis.db.get('pihouse/sprinkler/schedule/next')
	
	templateData = {
		'status' : status,
		'last_run' : last_run,
		'next_run' : next_run
	}
	
	return render_template('sprinkler.html', **templateData)

@app.route('/sprinkler/<action>')
#@register_breadcrumb(app, '.off', 'Sprinkler')
def action(action):
	if action == "on":
		if not redis.db.get('pihouse/sprinkler/status') == "True":
			mqtt.client.publish('pihouse/sprinkler/control', "True")

	if action == "off":
		mqtt.client.publish('pihouse/sprinkler/control', "False")
		mqtt.client.publish('pihouse/sprinkler/schedule/last', "request")

	sleep(0.2)
	return jsonify({'status': redis.db.get('pihouse/sprinkler/status')})

"""
	# Allow time for pin status to change
	sleep(0.2)
	status = redis.db.get('pihouse/sprinkler/status')
	last_run = redis.db.get('pihouse/sprinkler/schedule/last')
	next_run = redis.db.get('pihouse/sprinkler/schedule/next')

	templateData = {
		'status' : status,
		'last_run' : last_run,
		'next_run' : next_run
	}

	return render_template('sprinkler.html', **templateData)
"""
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
			# read schedule from db and pass as default field values
	elif request.method == 'POST' and form.validate_on_submit():
		schedule = '%s %s %s %s %s' %(str(form.minute.data), str(form.hour.data), str(form.dom.data), str(form.month.data), str(form.dow.data))
		mqtt.client.publish('pihouse/sprinkler/schedule', str(schedule))
		mqtt.client.publish('pihouse/sprinkler/schedule/set', str(form.use_schedule.data))
		flash('Schedule set!')
		#return redirect(url_for('sp_schedule'))

	return render_template('sp_schedule.html', title='Sprinkler Schedule',form=form)

"""
@app.route('/sprinkler/log')

"""