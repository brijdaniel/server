"""
Quick functions to change button appearance via js,
depending on current status / state changes

This is generic and used for sprinkler, windows etc 

Changelog: Major change, added lists for interchangibility
between terms. Removed 'switch' function as it was made redundant
by adding 'True'/'False' to the lists
"""
list_true = ['True', 'on', 'open', 'up']
list_false = ['False', 'off', 'closed', 'down']

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