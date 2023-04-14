"""
load image and pose from raw data
"""
from PIL import Image
import csv


class Frame:
    pass

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
        return frames

    def data(self, step):
        pass

    def align(self, frames):
        pass