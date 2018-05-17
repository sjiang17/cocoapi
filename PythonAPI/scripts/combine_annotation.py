import json
import os

annot_file_path = '/Users/siyu/Projects/dataset/coco/data/annotations/instances_val2017.json'
annot = json.load(open(annot_file_path, 'r'))

new_annot = {}
for key in annot:
    if not (key == 'images' or key == 'annotations'):
        new_annot[key] = annot[key]

images, annotations = [], []

per_img_annot_dir = '/Users/siyu/Projects/dataset/coco/flood_data/annotations/val'
annot_list = sorted([os.path.join(per_img_annot_dir, f)
                     for f in os.listdir(per_img_annot_dir) if f.endswith('.json')])

for ix, annot_file in enumerate(annot_list):
	if ix % 200 == 0:
		print ix
	per_annot = json.load(open(annot_file, 'r'))
	images.append(per_annot['image'])
	for obj in per_annot['annotation']:
		annotations.append(obj)

new_annot['images'] = images
new_annot['annotations'] = annotations
print len(new_annot['images']), len(new_annot['annotations'])

new_annot_file_path = '/Users/siyu/Projects/dataset/coco/flood_data/annotations/instances_val2017.json'
with open(new_annot_file_path, "w") as f:
	json.dump(new_annot, f, sort_keys=True, indent=2, ensure_ascii=False)