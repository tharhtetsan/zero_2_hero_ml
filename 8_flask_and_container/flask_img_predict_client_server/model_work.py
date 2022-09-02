import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2
import numpy as np

class modelWork:


    def __init__(self):
        
        self.model_path = r"D:\gans\git_upload\zero_2_hero_python\7_Deep_Learning\CNN\cats_and_dogs_classification\24_08_2022.h5"
        self.model = None
        self.keyMap = {
            0:"alphard",
            1:"corolla",
            2:"crown",
            3:"hilux",
            4 :"rav4"
            }

    def load_model(self):
        self.model= load_model(self.model_path)

    def predict_img_by_path(self,img_path):
        img= cv2.imread(img_path)
        img= cv2.resize(img,(256,256))
        img = np.array([img])      
        result = self.model.predict(img,batch_size =1)
        
        index = (np.argmax(result))
        return self.keyMap[index]

    def predict_img_by_arr(self,img):
        img= cv2.resize(img,(256,256))
        img = np.array([img])
        result = self.model.predict(img,batch_size =1)
        index = (np.argmax(result))
        return self.keyMap[index]