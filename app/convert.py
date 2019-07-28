"""
Quick functions to change button appearance via js,
depending on current status / state changes

This is generic and used for sprinkler, windows etc 
"""
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