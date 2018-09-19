from keras.preprocessing import image as image_utils
from imagenet_utils import decode_predictions
from imagenet_utils import preprocess_input
from vgg16 import VGG16
import numpy as np
import argparse
import cv2
import tensorflow as tf
import matplotlib.pyplot as plt

with tf.device('/gpu:0'):

 ap = argparse.ArgumentParser()
 ap.add_argument("-i", "--image", required=True, help="path to the input image")
 args = vars(ap.parse_args())

 orig = cv2.imread(args["image"])
 print("[INFO] loading and preprocessing image...")
 image = image_utils.load_img(args["image"], target_size=(224,224))
 image = image_utils.img_to_array(image)

 image = np.expand_dims(image, axis=0)
 image = preprocess_input(image)

 print("[INFO] loading network...")
 model = VGG16(weights="imagenet")

 print("[INFO] classifying image...")
 preds = model.predict(image)
 P = decode_predictions(preds)
 (inID, label, prob) = P[0][0]

 print("ImageNet ID: {}, Label: {}".format(inID, label))
 cv2.putText(orig, "Label: {}".format(label), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
 cv2.imshow("Classification", orig)
 cv2.waitKey(0)
