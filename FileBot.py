import os
import time
from datetime import date
from datetime import datetime

class FileBot:
	# folder_name = new folder where files will be relocated
	# location = the location of operation eg. "Desktop","Downloads" or "Documents"
	# file_name = the unique name to help identify file
	# file_exe = the file extension eg. "png" or "mov"
	def __init__(self,folder_name,location,file_name, file_exe, num_iteration):
		self.file_number = 0
		self.folder_name = folder_name
		self.location = location
		self.file_name = file_name
		self.file_exe = file_exe
		self.iteration = num_iteration
		self.temp_memory = []
		self.current_dir = None

	def _change_dir(self):
		dirx = os.getcwd()
		arr = dirx.split('/')
		path = '/'+arr[1]+'/'+arr[2]+'/'+ self.location
		os.chdir(path)
		self.current_dir = path

	def _get_date(self):
		today = date.today()
		return today.strftime("%d-%m-%Y")

	def _get_time(self):
		now = datetime.now()
		return now.strftime("%H:%M:%S")

	def _check_folder_exists(self):
		# Check if a screenshot folder exists, if not create one
		if os.path.exists(self.folder_name):
			path = self.current_dir + "/" + self.folder_name
			files = os.listdir(path)
			# update the number of files
			self.file_number = len(files)
		else:
			os.mkdir(self.folder_name)

	# Process 01
	def collect_files(self):
		files = os.listdir()
		for file in files:
			if '.' in file:
				file_split = file.split('.')
				file_nameX = file_split[0].split(' ')[0]
				if self.file_exe in file_split[-1:] and file_nameX == self.file_name:
					self.temp_memory.append(file)
	# Process 02
	def rename_and_relocate_files(self):
		for file in self.temp_memory:
			src = self.current_dir+ "/"+file
			dst = self.current_dir+"/"+self.folder_name+'/'+self.file_name+"_"+str(self.file_number + 1)+'.'+self.file_exe
			os.rename(src, dst)
			self.file_number += 1
		self.temp_memory = []

	def startBot(self):
		self._change_dir()
		self._check_folder_exists()
		life_cycles = 0
		running = True
		start_time = self._get_time()
		while running:
			time.sleep(5)
			current_time = self._get_time()
			print("File Name: " + self.file_name)
			print("Number of Files: " + str(self.file_number))
			print("Number of Cycles: " + str(life_cycles) +"/" + str(self.iteration))
			print("Time: " + current_time )
			print("=========================")
			self.collect_files()
			self.rename_and_relocate_files()
			if life_cycles >= self.iteration:
				running = False
				print("Task Completed ....")
			life_cycles += 1


if __name__ == "__main__":
	screenshotBot = FileBot('ScreenShot','Desktop','Screenshot','png',1000)
	screenshotBot.startBot()







