from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from scipy.io import loadmat
import numpy as np
import time
import pdb

time_start = time.time()

dir_tr = "C:/Users/tgolv/thesis/CODE/pytstuff/pca/"
dir_te = "C:/Users/tgolv/thesis/borrar/"
dir_predictions = "C:/Users/tgolv/thesis/borrar/"

dir_tr_hog_pca = "C:/hinterstoisser/final_descriptors/pca/"

labels = ['ape', 'cat', 'duck', 'bck']

x_tr = []
y_tr = []


print("Loading training data...")
xi = loadmat(dir_tr_hog_pca + "hog_tr_pca500.mat")

y_tr = xi['y_tr']


y_tr = np.hstack(y_tr)
z_tr = xi['z_tr']
x_tr = xi['x_tr']

print("Training...")
classifier = KNeighborsClassifier(n_neighbors=5, n_jobs=-1).fit(z_tr, y_tr)

print("Loading test data...")
z_te = loadmat(dir_predictions + "0000_rgb.mat")['z_te'][:, 3:]

print("Predicting labels...")
probabs = classifier.predict_proba(z_te)
        
print("Saving predictions...")
np.savetxt(dir_predictions + "0000_predict.txt", probabs, fmt="%f")






print("Time spent: " + str((time.time() - time_start)))