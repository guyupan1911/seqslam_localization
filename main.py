import data_loader

train_data = data_loader.DataLoader(
    '/home/yuxuanhuang/projects/mapping-experimental/data/bag/storge_xray_data/train0', 'autox').data(1.0)

query_data = data_loader.DataLoader(
    '/home/yuxuanhuang/projects/mapping-experimental/data/bag/storge_xray_data/test', 'autox').data(0.0)

