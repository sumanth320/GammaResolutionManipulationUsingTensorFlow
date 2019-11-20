#!/usr/bin/env python
# coding: utf-8

# In[9]:


from __future__ import absolute_import, division, print_function
from IPython.display import Image as IImage, display
import numpy as np
import PIL
from PIL import Image
import tensorflow as tf

# Load image to numpy array.
img = PIL.Image.open(r'C:\Users\Sumanth\Desktop\pic2.jpg')
img.load()
img_array = np.array(img)

def gamma_adjust(image):
   image = tf.image.adjust_gamma(image,6)
   return tf.cast(image, tf.uint8)

gamma_adjusted = gamma_adjust(img_array).numpy()
PIL.Image.fromarray(gamma_adjusted)

