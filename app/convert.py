def convert(status):
	if status == 'True':
		opposite = 'off'
	else:
		opposite = 'on'
	return opposite

def switch(status):
	if status == 'True':
		switch = 'on'
	else:
		switch = 'off'
	return switch