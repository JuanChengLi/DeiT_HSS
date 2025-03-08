"""Please put this file in the directory above martensite or bainite directory
 This figure will get into the bainite or martensite directory and create resized images /cropped images in the
 directory automatically Xiaohan Bie 2022-07-13 """

import os
import cv2 as cv
import matplotlib.pyplot as plt
import shutil


# this function loads all the images from a specified folder. change the size, and output in a dictionary
def load_images_from_folder(folder):
    input_images = {}
    for filename in os.listdir(folder):
        if filename[-3:] in ['png', 'jpg', 'gif', 'svg', 'peg']:
            magnification = (int(filename.split('X')[0]))
            change_ratio = desired_magnification / magnification
            img = cv.imread(os.path.join(folder, filename))
            [y_dim, x_dim] = img.shape[:2]
            print('xdim:', x_dim, 'y_dim', y_dim)
            x_dim = int(x_dim * change_ratio)
            y_dim = int(y_dim * change_ratio)
            img = cv.resize(img, (x_dim, y_dim))
            [x_dim, y_dim] = img.shape[:2]
            print('redized_xdim:', x_dim, 'redized_ydim', y_dim)

            if img is not None:
                input_images[str(filename)] = img
    return input_images


def save_resized_images_to_folder(input_images, input_path):
    if os.path.exists(input_path):
        shutil.rmtree(input_path)
    os.mkdir(input_path)
    os.chdir(path)
    for i in input_images.keys():
        print(input_images[i].shape)
        plt.imshow(input_images[i])
        plt.imsave(i, input_images[i])
        plt.show()


def gray(img):
    return cv.cvtColor(img, cv.COLOR_RGB2GRAY)


# images are defined in a dictionary
def crop_save(input_images, h, w, input_path):
    if os.path.exists(input_path):
        shutil.rmtree(input_path)
    os.mkdir(input_path)
    os.chdir(input_path)
    for i in input_images.keys():
        [y_dim, x_dim] = input_images[i].shape[:2]
        for y in range(int(y_dim / (0.5 * h))):
            for x in range(int(x_dim / (0.5 * w))):
                if x == (int(x_dim / (0.5 * w) - 1)) and y == (int(y_dim / (0.5 * h) - 1)):
                    cropped_img = input_images[i][-h:, -w:]
                elif x == (int(x_dim / (0.5 * w) - 1)):
                    cropped_img = input_images[i][int(0.5 * y * h):int((0.5 * y + 1) * h), -w:]
                elif y == (int(y_dim / (0.5 * h) - 1)):
                    cropped_img = input_images[i][-h:, int(0.5 * x * w):int((0.5 * x + 1) * w)]
                else:
                    cropped_img = input_images[i][int(0.5 * y * h):int((0.5 * y + 1) * h),
                                  int(0.5 * x * w):int((0.5 * x + 1) * w)]
                cv.imwrite(str(i) + str(y) + str(x) + '.png', cropped_img)

 
# main function start here


if __name__ == "__main__":

    # All the images are resized to 15000 magnification. You can change this value accordingly
    desired_magnification = 10000
    height = 672
    weight = 672
    desired_magnification = int(desired_magnification)

    current_path = r'C:\Users\xiaoh\Documents\BAINITE'
    for it in os.scandir(current_path):
        if it.is_dir() and it.name[-3:] == 'ITE':  # this part checks all the directories that contains figures
            os.chdir(os.path.join(current_path, it))
            print(os.getcwd())
            new_path = os.path.join(current_path, it)
            images = load_images_from_folder(new_path)
            path = new_path + '/size_changed'
            save_resized_images_to_folder(images, path)
            saved_path = new_path + '/cropped'
            crop_save(images, height, weight, saved_path)
            os.chdir(current_path)
