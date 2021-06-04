import configparser

class DotEnv:
	
	DEFAULT_FILE_NAME = '.env'

	def __init__(self):
		self.config = configparser.ConfigParser()
		self.file = DotEnv.DEFAULT_FILE_NAME
	
	@classmethod
	def as_ini(cls):
		cls.config = configparser.ConfigParser()
		cls.file = '.ini'
		return(cls)

env1 = DotEnv()
env2 = DotEnv.as_ini()


