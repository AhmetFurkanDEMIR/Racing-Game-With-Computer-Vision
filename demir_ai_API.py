import os
import time

try:

	import wget

	import tensorflow
	import pygame
	from pygame.locals import *

	import cv2

	import keras

	from keras_retinanet import models
	from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
	from keras_retinanet.utils.visualization import draw_box, draw_caption
	from keras_retinanet.utils.colors import label_color

	import numpy as np

	import imutils
	from imutils.video import VideoStream

except:

	os.system("cls" if os.name == "nt" else "clear")

	print("\n\n Gerekli modüller kuruluyor. Biraz uzun sürebilir...\n\n")

	time.sleep(1)

	os.system("python3 -m pip install --upgrade pip")

	os.system("pip3 install pygame")
	os.system("pip3 install opencv-python")
	os.system("pip3 install keras")
	os.system("pip3 install keras_retinanet")
	os.system("pip3 install numpy")
	os.system("pip3 install tensorflow-gpu")
	os.system("pip3 install imutils")

	os.system("cls" if os.name == "nt" else "clear")

	os.system("pip3 install wget")

	print("\n\n Gerekli modüller kuruldu. Hata durumunda Oyunu tekrar çalıştırınız.\n")

	time.sleep(1)


import wget

if not os.path.isfile(os.path.join("model.h5")):

	print("\n Model indiriliyor...")

	file_url1 = "https://www.dropbox.com/s/mfufsbj30c2twd2/model.h5?dl=1"
	wget.download(file_url1)

	os.system("cls" if os.name == "nt" else "clear")

	print("\n\n Model indirildi.")

	time.sleep(1)


import tensorflow as tf

if tf.test.gpu_device_name():

    print('Varsayılan GPU Cihazı : {}'.format(tf.test.gpu_device_name()))

else:

    print("Nvidia GPU Driver, CUDA V10.1 ve cuDNN V7.6.5 yazılımlarını yükleyiniz.")

    os.system("nvidia-smi")

    quit()



