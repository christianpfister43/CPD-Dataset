"""
@author: Christian Pfister
https://github.com/christianpfister43/CPD-Dataset

License: MIT: https://github.com/christianpfister43/CPD-Dataset/blob/main/LICENSE
"""

import numpy as np
from PIL import ImageGrab
import cv2
import time
import pandas as pd
import matplotlib.pyplot as plt
import os



#%% setting paths and parameters
#finetuning these parameters will require some manual work on your specific screen
save_path = '../data'
label_file_name = 'labels.csv'

number_of_digits = 10 # numbers 0-9
number_of_cols = 15 # 15 columns of numbers 0-9
w = 20  # width of the digit image taken
h = 24  # height of the digit image taken
x_0 = 203  # starting point on your screen in x
y_0 = 236  # starting point on your screen in y
x_correction = 0 # correction parameter if needed
delta_x = 24  # sliding the image window in x direction
delta_y = 30  # sliding the image window in y direction

#%% If the label file exist, the dataset will be extended, otherwise a new set created

if os.path.isfile(f'{save_path}/{label_file_name}'):
    labels = pd.read_csv(f'{save_path}/labels.csv')
    i=0
else:
    labels = pd.DataFrame(columns=['image_name','label'])
    i=len(labels)

#%%Loop over columns and rows of digits

for n in range (number_of_cols):
    for m in range(number_of_digits):
        printscreen_pil = ImageGrab.grab(bbox=(x_0+n*delta_x + x_correction,y_0+m*delta_y,x_0+n*delta_x+w + x_correction,y_0+h+m*delta_y))
        image = np.array(printscreen_pil.getdata(), dtype='uint8')\
            .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))
        
        digit_image = cv2.resize(image, (28,28))      # 28*28 format of MNIST dataset
        img_gray = cv2.cvtColor(digit_image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f'{save_path}/images/digit_image{i}.png',img_gray) # saving the image as gray_scale
        # cv2.imwrite(f'{save_path}/images/digit_image{i}.png',digit_image) # your can use this to save as color image
        labels = labels.append({'image_name':f'digit_image{i}.png','label':m},ignore_index=True)
        i+=1

#%%saving the labesl file

if os.path.isfile(f'{save_path}/{label_file_name}'):
    labels.to_csv(f'{save_path}/labels_new.csv',index=False)    # if your labels.csv already exist, dont overwrite it, create a new to be save
else:
    labels.to_csv(f'{save_path}/{label_file_name}',index=False)






















