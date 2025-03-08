## Please put this file in the directory above martensite or bainite directory 
## This figure will get into the bainite or martensite directory and create resized images /cropped images in the directory automatically
## Xiaohan Bie 2022-07-13


##
import PIL
from PIL import Image
import os
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import shutil


## All the images are resized to 15000 magnification. You can change this value accordingly
desired_magnification=10000
height = 672
weight = 672
desired_magnification=int(desired_magnification)




#this function loads all the images from a specified folder. change the size, and output in a dictionary
def load_images_from_folder(folder):
    images = {}
    for filename in os.listdir(folder):
        if filename[-3:] in ['png','jpg','gif','svg','peg']:
            magnification=(int(filename.split('X')[0]))
            change_ratio=desired_magnification/magnification
            img = cv.imread(os.path.join(folder,filename))
            [y_dim,x_dim]=img.shape[:2]
            print('xdim:',x_dim,'y_dim',y_dim)
            x_dim=int(x_dim*change_ratio)
            y_dim=int(y_dim*change_ratio)
            img = cv.resize(img,(x_dim,y_dim))
            [x_dim,y_dim]=img.shape[:2]
            print('redized_xdim:',x_dim,'redized_ydim',y_dim)
 
            if img is not None:
                images[str(filename)]=(img)
    return images
	
	
def save_resized_images_to_folder(images,saved_path):
    if  os.path.exists(saved_path):
        shutil.rmtree(saved_path)
    os.mkdir(saved_path)
    os.chdir(path)
    for i in images.keys():
        print(images[i].shape)
        plt.imshow(images[i])
        plt.imsave(i,images[i])
        plt.show()
		
		
def gray(img):
  return cv.cvtColor(img, cv.COLOR_RGB2GRAY)
		
#images are defined in a dictionary
def cropSave(images, h, w, saved_path):
    if  os.path.exists(saved_path):
        shutil.rmtree(saved_path)
    os.mkdir(saved_path)
    os.chdir(saved_path)
    for i in images.keys():
        [y_dim,x_dim]=images[i].shape[:2]
        for y in range(int(y_dim / (0.5*h))):
            for x in range(int(x_dim/ (0.5*w))):
                if x==(int(x_dim/ (0.5*w)-1)) and y==(int(y_dim / (0.5*h)-1)):
                    cropped_img = images[i][-h:, -w:]
                elif  x==(int(x_dim/ (0.5*w)-1)) :
                    cropped_img = images[i][int(0.5*y*h):int((0.5*y+1)*h), -w:]
                elif  y==(int(y_dim / (0.5*h)-1)):
                    cropped_img = images[i][-h:, int(0.5*x*w):int((0.5*x+1)*w)]
                else:
                    cropped_img = images[i][int(0.5*y*h):int((0.5*y+1)*h), int(0.5*x*w):int((0.5*x+1)*w)]
                cv.imwrite(str(i) + str(y) + str(x) +'.png' ,cropped_img)

				
				
########main function start here

current_path = os.getcwd()
for it in os.scandir(current_path):
    if it.is_dir() and it.name[-3:] =='ITE': # this part checks all the directories that contains figures
        os.chdir(os.path.join(current_path, it))
        print(os.getcwd())
        new_path=os.path.join(current_path, it)
        images=load_images_from_folder(new_path)
        path=new_path+'/size_changed'  
        save_resized_images_to_folder(images,path)
        saved_path=new_path+'/cropped'
        cropSave(images, height, weight, saved_path)
        os.chdir(current_path)
