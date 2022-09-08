import numpy as np
import pdb
import os
from pathlib import Path
import glob
import cv2
from shutil import copyfile



dir_gt = "C:/hinterstoisser/final_gt/"
dest_train = "C:/hinterstoisser/yolo_transf/train/images/"
dest_labels = "C:/hinterstoisser/yolo_transf/train/labels/"

labels = ['ape', 'bck', 'cat', 'duck']

i=0
label='ape'
j=0
for f in glob.glob(dir_gt + label + "/*.png"):

	name_img = f[len(dir_gt+label)+1:-4]
	new_name = name_img + '_' + str(i) 
	copyfile(f, dest_train + new_name + '.png')
	#shutil.copy(src_file,dest_dir) #copy the file to destination dir

	# dst_file = os.path.join(dest_train, name_img + '.png')
	# new_dst_file_name = os.path.join(dest_train, new_name + '.png')
	# os.rename(dest_train, new_dst_file_name) #rename

	im = cv2.imread(f)
	y_axis = im.shape[0]
	x_axis = im.shape[1]

	file1 = open(dest_labels+ new_name + ".txt","a")
	file1.write( str(i) + ' 0.5 0.5 1 1\n')
	file1.close()

	j+=1
	if j>5:
		break
# copiar y nombrar cada imagen con nombre_ a b c d al final en una misma carpeta train
# hacer lo de los txt segun etiuetas del tutorial nueva carpeta labels
# 
# pillar las de test, renombrarlas segun mismo criterio y meterlas en una misma carpeta TEST

# After using a tool like CVAT, makesense.ai or Labelbox to label your images, export your labels to YOLO format, with one *.txt file per image
# (if no objects in image, no *.txt file is required). The *.txt file specifications are:

# One row per object
# Each row is class x_center y_center width height format.
# Box coordinates must be in normalized xywh format (from 0 - 1). 
# If your boxes are in pixels, divide x_center and width by image width, and y_center and height by image height.
# Class numbers are zero-indexed (start from 0).        