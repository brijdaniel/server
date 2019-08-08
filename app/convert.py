"""
Quick functions to change button appearance via js,
depending on current status / state changes

This is generic and used for sprinkler, windows etc 

Changelog: Major change, added lists for interchangibility
between terms. Removed 'switch' function as list capability
added to convert means I can just use on/off etc as status'
instead of having to use true/false and then convert
"""
list_true = ['on', 'open', 'up']
list_false = ['off', 'closed', 'down']

def convert(status):
	if status in list_true:
		opposite = list_false[list_true.index(status)]
		return opposite
	elif status in list_false:
		opposite = list_true[list_false.index(status)]
		return opposite

def switch(status):
	if status == 'True':
		switch = 'on'
	else:
		switch = 'off'
	return switch