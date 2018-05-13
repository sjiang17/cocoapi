import os
import shutil

annot_dir = '/fldata/dataset/coco/flood_data/original/val'
save_dir = '/fldata/dataset/coco/flood_data/mask/val'
annot_files = sorted([os.path.join(annot_dir, f)
                      for f in os.listdir(annot_dir) if f.endswith('.json')])

for ix, annot_file in annot_files:
	if ix == 2000:
		break
	dst_file = os.path.join(save_dir, os.path.basename(annot_file))
	shutil.copyfile(annot_file, dst_file)