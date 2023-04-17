"""
load image and pose from raw data
"""
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import csv
import numpy as np
import os

class Frame:
    def __init__(self, image_uri, pose):
        if os.path.exists(image_uri):
            self.image_uri = image_uri
            self.image = cv2.imread(self.image_uri)
            cv2.imshow('image', self.image)
            cv2.waitKey(5)
        else:
            print('image_uri: ', image_uri, ' doesn\'t exist')
        self.pose = pose

class DataLoader:
    def __init__(self, path, data_source):
        if data_source == 'autox':
            self.frames = self.add_frames_autox(path)
        elif data_source == '4seasons':
            self.frames = self.add_frames_4seasons(path)

    def add_frames_autox(self, path):
        frames=[]
        lidar_pose = path + '/lidar.csv'
        with open(lidar_pose) as file:
            print(file.read())
        timestamp = path + '/image_and_pose.txt'

        # read image_uri and timestamp
        with open(timestamp) as file:
            pass
        return frames

    def add_frames_4seasons(self, path):
        frames = []
        image_dir = path + '/distorted_images/cam0'
        gnss_txt = path + '/GNSSPoses.txt'
        lines = np.loadtxt(gnss_txt, delimiter=',')
        for i in lines:
            frame = Frame(image_dir+'/'+str(int(float(i[0])))+'.png', i[1:8])
            frames.append(frame)
        return frames

    def data(self, step):
        return self.frames

    def align(self, frames):
        pass