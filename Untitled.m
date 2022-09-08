close all
clear all
clc



t = cputime;

% CONSTANTS
win_hog = 8;
slid_win_size = [96 96];
slid_win_period = 1;
nlevels = 4;
scale = 1.2;
IoU_threshold = 0.5; % Threshold for intersection over union
nclasses = 4;
hog_mode = 'depth';

height = slid_win_size(2);
width = slid_win_size(1);
boxes_matrix = [];

add_ape_test = 'C:\hinterstoisser\test\ape\rgbd\';
add_pca_training = 'C:\hinterstoisser\final_descriptors\pca\';


current_file_name = horzcat(add_ape_test, '0000_depth.png');
ima = imread(current_file_name);

% ima = im(125:300,180:471,:);
addpath('C:\Users\tgolv\thesis\CODE\pytstuff\execute_me_just_once')

[piramide, v_scales] = impyram(ima,nlevels, scale);

[sw_matrix] = f_sw_image(ima, nlevels, scale, win_hog, slid_win_size, slid_win_period, hog_mode);