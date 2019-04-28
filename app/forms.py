from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class SpTimer(FlaskForm):
	timer = DecimalField('timer', validators=[DataRequired()], places=2)
	submit = SubmitField('Timer Set')

class SpScheduleForm(FlaskForm):
    minute = StringField('minute', validators=[DataRequired()])
    hour = StringField('hour', validators=[DataRequired()])
    dom = StringField('dom', validators=[DataRequired()])
    month = StringField('month', validators=[DataRequired()])
    dow = StringField('dow', validators=[DataRequired()])
    use_schedule = BooleanField('Use Schedule')
    submit = SubmitField('Update Schedule')