import os
import json
import numpy as np

class my_coco():
	def __init__(self, img_dir='', annot_dir=''):
		self._dir = dir
		# assert os.path.exists(self._dir), 'Kitti data directory does not exist'
		self._img_dir = img_dir
		self._annot_dir = annot_dir
		# self._num_classes = 2
		# self._classes = ('__background__',  # always index 0
  #                    'car')
		# self._class_to_ind = dict(list(zip(self._classes, \
		# 						list(range(self._num_classes)))))

	def _list_imgs(self):
		img_files = [os.path.join(self._img_dir, f.split('.json')[0]\
						 + '.jpg') for f in sorted(os.listdir(self._annot_dir)) if f.endswith('.json')]
		return img_files 

	def _list_annots(self):
		assert os.path.exists(self._annot_dir), 'Coco data directory does not exist: {}'.format(self._annot_dir)
		annot_files = [os.path.join(self._annot_dir, f) for f in \
							sorted(os.listdir(self._annot_dir)) if f.endswith('.json')]
		return annot_files

	def _read_annot(self, annot_file):
		# print annot_file
		annot = json.load(open(annot_file, 'r'))
		num_objs = len(annot['annotation'])
		boxes = np.zeros((num_objs, 4), dtype=np.uint16)
		gt_classes = np.zeros(num_objs, dtype=np.int32)
		boxes_area = np.zeros(num_objs, dtype=np.float32)

		for ix, obj in enumerate(annot['annotation']):
			x, y, w, h = obj['bbox']
			boxes[ix, :] = [x, y, x+w, y+h]
			boxes_area[ix] = obj['area']
			gt_classes[ix] = obj['category_id']

		return {'boxes': boxes,
				'gt_classes': gt_classes,
				'areas': boxes_area}