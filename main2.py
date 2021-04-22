from PIL import Image
from numpy import asarray
import os
import fnmatch
import numpy
import sys
import time
start_time = time.time()
#full array setting
numpy.set_printoptions(threshold = sys.maxsize)
#file counting
files_counting = len(fnmatch.filter(os.listdir("New folder"), '*.png'))
#images array
images_array = []
for i in range(files_counting - 1):
    image = Image.open('New folder/out'+str(i+1)+'.png')
    data = asarray(image)
    images_array.append(data)
print(time.time()-start_time)
print(images_array[1])




