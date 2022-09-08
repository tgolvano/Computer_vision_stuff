from scipy.io import loadmat
from sklearn.metrics import average_precision_score
import numpy as np
import time
import pdb



time_start = time.time()


dir_predictions = "C:/Users/tgolv/thesis/borrar/"



print("Loading detection data...")
final_boxes_labeled = loadmat(dir_predictions + "0000_detections.mat")["final_boxes_labeled"]

# final_boxes_labeled  STRUCTURE:
# Each row is one different detection of the object
# [labels(k), probability(k), px_row, px_col, w, h, IoU_label]
# IoU_label is binary, it is calculated between Ground Truth and Bounding Box Detection
# if Intersection/Union > IoU_threshold ===> IoU_label = 1 		else IoU_label = 0



y_true = np.array(final_boxes_labeled[:,6])
y_scores = np.array(final_boxes_labeled[:,1])

mAP = average_precision_score(y_true, y_scores)  

print("mAP = " + str(mAP))