"""
Σύνολο συναρτήσεων που 
υλοποιήσαμε για την εργασία.
"""

import matplotlib.pyplot as plt
import cv2
import numpy as np
from skimage.util import img_as_float, img_as_ubyte                                          
from skimage.segmentation import slic, mark_boundaries

def plot_image(image, title=None):
    """"
    Δέχεται σαν όρισμα array μιας εικόνας, έναν τίτλο
    και εμφανίζει την εικόνα
    """
    if title is not None:
        plt.title(title)
    plt.imshow(image)

def rgb2lab(rgb_image):
    """
    Δέχεται σαν όρισμα μια rgb εικόνα και την μετατρέπει σε lab
    """
    return cv2.cvtColor(rgb_image, cv2.COLOR_RGB2LAB)

def lab2rgb(lab_image):
    """
    Δέχεται σαν όρισμα μια lab εικόνα και την μετατρέπει σε rgb
    """
    return cv2.cvtColor(lab_image, cv2.COLOR_LAB2RGB)

def rgb2gray(image):
    """"
    Δέχεται σαν όρισμα μια εικόνα και την επιστρέφει σε grayscale
    """
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return image

def subplot_in_row_images(images, titles, height=20, width=20):
    """
    Συνάρτηση που εμφανίζει σε μια σειρά τις εικόνες
    με τους αντίστοιχους τίτλους
    """
    f, axarr = plt.subplots(1,len(images))
    f.set_figheight(height)
    f.set_figwidth(width)
    for i in range(len(titles)):
        axarr[i].title.set_text(titles[i])
        axarr[i].imshow(images[i])
        
