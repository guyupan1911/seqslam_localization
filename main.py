import data_loader
import visualization

train_data = data_loader.DataLoader(
    '/home/guyupan/dataset/4seasons/PARKING_GARAGE/parking_garage_1_train', '4seasons').data(1.0)
print('train_data size: ', len(train_data))
query_data = data_loader.DataLoader(
    '/home/guyupan/dataset/4seasons/PARKING_GARAGE/parking_garage_2_train', '4seasons').data(0.0)
print('query_data size: ', len(query_data))

# visualization.display_frames_path(train_data)
visualization.display_frames_path(query_data)
