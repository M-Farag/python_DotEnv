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
	
	'''
	' Check if the Env file exists
	' @auther Mina <mina.farag@icloud.com>
	'''
	def is_file_exist(self):
		return path.exists(self.file_name)
	
	'''
	' Read from the env file
	' you will provide the key and the method will return the value
	' @auther Mina <mina.farag@icloud.com>
	'''
	def read(self,key_name:str,section='main'):
		if self.is_file_exist():
			self.config.read(self.file_name)
			return self.config[section].get(key_name)


