import os
import shutil

img_list = '/fldata/dataset/coco/flood_data/annotations/train.txt'
src_dir = '/fldata/dataset/coco/train2017'
save_dir = '/fldata/dataset/coco/mask/train/0'

with open(img_list, 'r') as f:
	selected_files = [l.strip('\n') for l in f.readlines()]

for base_name in selected_files:
	src_file = os.path.join(src_dir, base_name + '.jpg')
	dst_file = os.path.join(save_dir, base_name + '.jpg')
	shutil.copyfile(src_file, dst_file)
