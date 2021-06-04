import configparser
from os import path

class DotEnv:
	
	DEFAULT_FILE_NAME = '.env'
	
	'''
	' Main Constructor
	'''
	def __init__(self):
		self.config = configparser.ConfigParser()
		self.file_name = DotEnv.DEFAULT_FILE_NAME
	
	'''
	' Alternative constructor incase you want to initialize the 
	' Env file with a different extension
	' @auther Mina <mina.farag@icloud.com>
	'''
	@classmethod
	def as_file_name(cls,file_name='.ini'):
		cls.config = configparser.ConfigParser()
		cls.file_name = file_name
		return(cls)

	'''
	' Create/init the env file for the first time
	' @auther Mina <mina.farag@icloud.com>
	'''
	def create_file(self):
		self.config['main'] = {
			"key_1":"value_1"
		}
		with open(self.file_name,'w') as configfile:
			self.config.write(configfile)
	

	def is_exist(self):
		return path. exists(self.file_name)

