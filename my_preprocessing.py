"""
dataset from LDPolypVideo Benchmark: A Large-Scale Colonoscopy Video Dataset of Diverse Polyps
https://link.springer.com/chapter/10.1007/978-3-030-87240-3_37

dataset from Li et al is a serises of jpgs
images are cropped via mask
processed data saved in object called  SfMDataset(Dataset):

"""

import cv2 
import os
import sys

""" 
converts avi video files to jpgs
code from https://gist.github.com/megabudino/25eaadd2ea5dd9c1ceb6129704dd9a08
"""
class avi2jpg:    
    def convert(self, video, jpg_folder_filepath):
        vidcap = cv2.VideoCapture(video)
        success,image = vidcap.read()
        count = 0
        while success:
            framecount = "{number:06}".format(number=count)
            filename = jpg_folder_filepath+"/"+framecount+".jpg"
            cv2.imwrite(filename, image)     # save frame as JPEG file      
            success,image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1

"""
save frame by frame jpgs of videos
"""
def save_frames_from_videos(vid_folder_filepath, jpg_folder_filepath):

    converter = avi2jpg()
    os.mkdir(jpg_folder_filepath)

    for video in os.listdir(vid_folder_filepath):
        converter.convert(video)




