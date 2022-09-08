from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from scipy.io import loadmat
import numpy as np
import time
import pdb
import glob
import os

folder = 'C:/hinterstoisser/test_rgb/ape/'



imagefiles = glob.glob( folder + 'sw_hog_pca_*.mat')
nfiles = len(imagefiles)  # Number of files found
# first_part_name = len(folder+'sw_hog_pca_')
# identity_name = imagefiles[5][first_part_name:-4]
# print(identity_name)
#number_names = imagefiles( [folder + 'sw_hog_pca_', something , '.mat'] )
destination_folder = folder + '/predictions/' + 'pca100_' + 'nn/'
print(destination_folder)

#os.mkdir(folder + '/predictions/' + 'pca100_' + 'nn/')


labels = ['ape', 'cat', 'duck', 'bck']

dir_te = 'C:/hinterstoisser/test_rgb/'
for k in range(1,15):

    print("Training... k = " + str(k))

    for i, label in enumerate(labels):
        if label in 'bck':
            break
        print("Loading " + label + "...") 
        destination_folder = dir_te + label + '/predictions/pca100_' + str(k) + 'nn/'

        imagefiles = glob.glob( dir_te + label + '/sw_hog_pca_*.mat')
        nfiles = len(imagefiles)
       
        for j in range(50):
            print(j)
# for k in range(len(imagefiles)):
#     first_part_name = len(folder+'sw_hog_pca_')
#     identity_name = imagefiles[k][first_part_name:-4]
#     print(identity_name)