from openpyxl import Workbook
import os, glob

class Pixl():
	def __init__(self, image, workbook_name="default", folder = "user_files"):
		self.image = image
		self.workbook_name = workbook_name
		self.wb = Workbook()
		self.folder = folder
		if not os.path.exists(folder):
			os.makedirs(folder)

	def create_workbook(self):
		files = glob.glob(self.folder + "/" + self.workbook_name+"*.xls")
		if files:
			new_number = len(files)
			self.wb.save(self.folder+"/"+self.workbook_name+"{}.xls".format(new_number))
		else:
			self.wb.save(self.folder+"/"+self.workbook_name+".xls")

