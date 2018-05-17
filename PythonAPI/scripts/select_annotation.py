import os
import json
from collections import defaultdict

# ['person', 'bicycle', 'car', 'motorcycle', 'airplane',
#  'bus', 'train', 'truck', 'boat', 'cat', 'dog', 'horse', 'sheep',
#  'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'banana', 'apple',
#  'orange', 'pizza', 'cake', 'toilet', 'tv', 'laptop', 'keyboard',
#  'cell' 'phone', 'microwave', 'oven', 'sink', 'refrigerator',
#  'book', 'clock', 'vase', 'teddy bear']
cls_to_keep = [1, 2, 3, 4, 5, 6, 7, 8, 9, 17, 18, 19, 20, 21, 22, 23, 24,
               25, 52, 53, 55, 59, 61, 70, 72, 73, 76, 78, 79, 81, 82, 84, 85, 86, 88]

annot_dir = '/fldata/dataset/coco/original/annotations/train' 
save_dir = '/fldata/dataset/coco/flood_data/annotations/train'
imgset_file = '/fldata/dataset/coco/flood_data/annotations/train.txt'
num_to_keep = 30000
annot_files = sorted([os.path.join(annot_dir, f)
                      for f in os.listdir(annot_dir) if f.endswith('.json')])

img_names = []
num_kept = 0
for annot_file in annot_files:
    if num_kept == num_to_keep:
        break
    keep = False
    annot = json.load(open(annot_file, 'r'))
    new_annot = dict()
    new_annot['image'] = annot['image']
    obj_list = []
    for obj in annot['annotation']:
        if obj['category_id'] not in cls_to_keep:
            continue
        if obj['iscrowd'] == 1:
            continue
        keep = True
        obj.pop('segmentation')
        obj_list.append(obj)

    if keep:
	num_kept += 1
    	new_annot['annotation'] = obj_list
        basename = os.path.basename(annot_file)
        save_file = os.path.join(save_dir, basename)
        with open(save_file, "w") as f:
            json.dump(new_annot, f, sort_keys=True, indent=2)
        img_names.append(basename.strip('.json'))

img_names.sort()
with open(imgset_file, "w") as f:
    f.write("\n".join(img_names))
