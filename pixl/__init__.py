import sys
import os
import glob

try:
	from openpyxl import Workbook
	import matplotlib.image as mpimg
except:
	raise Exception("Please install all the required modules!")

class FileNotFoundError(Exception):
	"""
	This exception will be raised if the
	image file is not found
	"""
	pass

class Pixl():
	def __init__(self, image, workbook_name="default", folder = "user_files"):
		self.image = image
		self.workbook_name = workbook_name
		self.wb = Workbook()
		self.folder = folder
		if not os.path.exists(folder):
			os.makedirs(folder)

	def __openimage__(self):
		try:
			image_array = mpimg.imread(self.image)
		except:
			raise FileNotFoundError("Image file not found!")

	def __fillimage__(self):
		"""
		This function will call the __openimage__
		function and fill each and every cell in the
		excel sheet with the pixel values given
		"""
		pass

	def create_workbook(self):
		self.__openimage__()
		files = glob.glob(self.folder + "/" + self.workbook_name+"*.xls")
		if files:
			new_number = len(files)
			self.wb.save(self.folder+"/"+self.workbook_name+"{}.xls".format(new_number))
		else:
			self.wb.save(self.folder+"/"+self.workbook_name+".xls")

