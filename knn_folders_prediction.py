from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn import svm, grid_search

from scipy.io import loadmat
import numpy as np
import time
import pdb
import glob
import os

time_start = time.time()



dir_tr_hog_pca = "C:/hinterstoisser/final_descriptors/"

labels = ['ape', 'cat', 'duck', 'bck']
modes = ['depth', 'rgbd', 'grayscale']

x_tr = []
y_tr = []


for m, mode in enumerate(modes):
    
    dir_te = 'C:/hinterstoisser/test_' + mode + '/'

    



    for pca_ncomponents in [100, 500]:

        print("Loading training " + mode + " data...")
        xi = loadmat(dir_tr_hog_pca + mode + "/hog_tr_"+mode+"_pca" + str(pca_ncomponents) + ".mat")

        y_tr = xi['y_tr']


        y_tr = np.hstack(y_tr)
        z_tr = xi['z_tr']
        x_tr = xi['x_tr']



        for k in [15]:#[2,5,8,10,15]:

            print("Training... k = " + str(k))
            classifier = KNeighborsClassifier(n_neighbors=k, n_jobs=-1).fit(z_tr, y_tr)

            for i, label in enumerate(labels):
                
               

                if label in 'bck':
                    break
                
                print("Loading " + label + "...") 
                destination_folder = dir_te + label + '/predictions/pca' + str(pca_ncomponents) +'_' + str(k) + 'nn/'
                os.mkdir(destination_folder) # create folder

                imagefiles = glob.glob( dir_te + label + '/sw_hog_pca'+str(pca_ncomponents) + '_*.mat')

                for j in range(20):
                    first_part_name_length = len(dir_te + label +'/sw_hog_pca'+str(pca_ncomponents)+'_')

                    image_name = imagefiles[j][first_part_name_length:-4]

                    print("Loading test data...")
                    z_te = loadmat(imagefiles[j])['z_te'][:, 3:]

                    print("Predicting labels...")
                    probabs = classifier.predict_proba(z_te)
                        
                    print("Saving predictions..." + "image " + str(j)+ ' '+label+ ' '+mode+ ' PCA ' + str(pca_ncomponents)+' k='+str(k))
                    np.savetxt(destination_folder + image_name + "predictions.txt", probabs, fmt="%f")


print("Time spent: " + str((time.time() - time_start)))