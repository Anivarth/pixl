from pixl import Pixl
import pytest, glob, random
import numpy as np
import matplotlib.pyplot as plt

def test_workbook_name():
	"""
	This function will test if the 
	pixl function is accepting the
	name of the workbook"""
	px = Pixl(image = "pp.jpg", workbook_name = "test_workbook", folder = "test_folder")
	px.create_workbook()
	files = glob.glob("test_folder/*.xls")
	assert "test_folder/test_workbook.xls" in files

def test_default_values():
	"""
	This will test will fail if the name is not provided
	"""
	px = Pixl(image = "pp.jpg", )
	px.create_workbook()
	files = glob.glob("user_files/*.xls")
	assert "user_files/default.xls" in files

def test_duplicate_file_names():
	"""
	this will test if the same names are given for
	many calls
	"""
	random_number = str(random.randint(1, 1000))
	px = Pixl(image = "pp.jpg", workbook_name = random_number)
	px1 = Pixl(image = "pp.jpg", workbook_name = random_number)
	px2 = Pixl(image = "pp.jpg", workbook_name = random_number)
	px.create_workbook()
	px1.create_workbook()
	px2.create_workbook()
	files = glob.glob("user_files/"+random_number+"*.xls")
	assert len(files) == 3

def test_image_input():
	"""
	test to give the image file name"""
	# create random image
	image_pixel_values = np.random.rand(10, 10, 3)
	random_image = plt.imshow(image_pixel_values)
	plt.axis("off")
	plt.savefig("test_image.png", bbox_inches = "tight")
	px = Pixl(image = "test_image.png")

def test_image_file_not_found():
	"""
	test to raise error if the image file is not found"""
	with pytest.raises("FileNotFoundError"):
		px = Pixl(image = "ThisFileIsNotThere.png")
