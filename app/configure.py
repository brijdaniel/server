from configparser import ConfigParser

class Configure(ConfigParser):
	def __init__(self):
		super(Configure, self).__init__()
		self.file = '/home/server/server/app/config.ini'
		self.config = ConfigParser()
		self.config.read(self.file)

	def read(self, section, key):
		return self.config.get(section, key)

	def set(self, section, key, value):
		self.config.set(section, key, value)
		with open ('/home/server/server/app/config.ini','w') as file:
			self.config.write(file)