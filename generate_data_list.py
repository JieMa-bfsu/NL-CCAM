""" Generate lists containing filepaths and labels for training, validation and evaluation. """
import pickle
import os.path
import random

##### generate training set #####
TRAIN_Fore_Dir = '/sdb2/MJ/dataset/brisbane_746+457/train/fore/'
TRAIN_Back_Dir = '/sdb2/MJ/dataset/brisbane_746+457/train/back/'
TEST_DIR_FORE = '/sdb2/MJ/dataset/brisbane_746+457/validation/fore/'
TEST_DIR_BACK = '/sdb2/MJ/dataset/brisbane_746+457/validation/back/'

# TRAIN_Fore_Dir = '/sdb2/MJ/dataset/geo_151+129/train/residential/'
# TRAIN_Back_Dir = '/sdb2/MJ/dataset/geo_151+129/train/back/'
# TEST_DIR_FORE = '/sdb2/MJ/dataset/geo_151+129/validation/back/'
# TEST_DIR_BACK = '/sdb2/MJ/dataset/geo_151+129/validation/residential/'


train_set_list = []
test_set_list = []
with open("bris/train_list.txt","w") as f:
    for file_name in os.listdir(TRAIN_Fore_Dir):
            img_path = os.path.join(TRAIN_Fore_Dir, file_name)
            if  os.path.exists(img_path) :
                f.write(img_path+';'+'1\n')

    for file_name in os.listdir(TRAIN_Back_Dir):
        img_path = os.path.join(TRAIN_Back_Dir, file_name)
        if  os.path.exists(img_path):
            f.write(img_path+';'+'0\n')

##### generate test set #####

with open("bris/test_list.txt","w") as f:
    for file_name in os.listdir(TEST_DIR_FORE):
            img_path = os.path.join(TEST_DIR_FORE, file_name)
            if  os.path.exists(img_path) :
                f.write(img_path+';'+'1\n')

    for file_name in os.listdir(TEST_DIR_BACK):
        img_path = os.path.join(TEST_DIR_BACK, file_name)
        if  os.path.exists(img_path):
            f.write(img_path+';'+'0\n')


