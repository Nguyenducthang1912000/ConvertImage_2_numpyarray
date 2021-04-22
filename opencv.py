#import library
import cv2
import numpy
import sys
import fnmatch
import shutil
import os

#full array setting
numpy.set_printoptions(threshold = sys.maxsize)

#working directory
working_directory = "D:\\Opencv_tutorial\\"

#video link
link = "short.mp4"
name = link.split('.')

#split audio file from video file
os.system(f'cmd /c "ffmpeg -i {link} -c:a libmp3lame -q:a 4 {name[0]}.mp3"')

#take video fps
cap=cv2.VideoCapture(link)
fps = cap.get(cv2.CAP_PROP_FPS)

#create a folder that contain video
dir = working_directory + name[0]
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)

#move audio file into the same folder as img files
shutil.move(f'{working_directory}{name[0]}.mp3',f'{working_directory}{name[0]}')

#move to folder contain video
os.chdir(working_directory + name[0])

#video to image converter
os.system(f'cmd /c "ffmpeg -i {working_directory}{link} -vf fps={fps} out%d.png"')
os.chdir(working_directory)

#file counting
files_counting = len(fnmatch.filter(os.listdir(name[0]), '*.png'))

#images array
images_array = []


# def main():
for i in range(files_counting - 1):
    im = cv2.imread(f'{name[0]}/out{i+1}.png')
    img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    images_array.append(img)
# if __name__ == "__main__":
#     main()
print(type(images_array[0]))



