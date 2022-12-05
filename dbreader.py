import cv2
import numpy as np
import pandas as pd

print('reading...')
db = pd.read_pickle(r'dev_letter_D.p')

print("Number of letter images in the dataset are:" + str(len(db)))

#The dataset contains 7702 images of sanskrit letters belonging to 602 classes
#The dataset is structured in the following manner:
	#The data array is a 2D array
	#The first index is for the mth element in the array or mth letter in the data
	#The second index is used for the following:
		# Each row of the 2D array contains an image, its corresponding class index number and its English class Annotation

#Please run the code below see an Example


for i in range(1,6):
	#cv2.imshow('a',db[i][-1])
	#cv2.waitKey()
	print("The Class index  : " + str(db[:-i][1]))
	print("English Class Annotation : " + str(db[:-i][2]))
	print()