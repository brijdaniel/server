from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from app import redis

class SpTimer(FlaskForm):
	timer = DecimalField('timer', validators=[DataRequired()], places=2, default=float(redis.db.get('pihouse/sprinkler/timer')))
	submit = SubmitField('Set Timer')

class SpScheduleForm(FlaskForm):
	schedule = redis.db.get('pihouse/sprinkler/schedule').split()
	minute = StringField('minute', validators=[DataRequired()], default=schedule[0])
	hour = StringField('hour', validators=[DataRequired()], default=schedule[1])
	dom = StringField('dom', validators=[DataRequired()], default=schedule[2])
	month = StringField('month', validators=[DataRequired()], default=schedule[3])
	dow = StringField('dow', validators=[DataRequired()], default=schedule[4])
	use_schedule = BooleanField('Use Schedule', default='checked')
	submit = SubmitField('Update Schedule')