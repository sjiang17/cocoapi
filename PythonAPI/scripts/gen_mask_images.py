import random
import cv2
from my_coco import my_coco
import numpy as np
import os
import sys
import shutil
import copy

def create_dir(path):
	if not os.path.exists(path):
		os.makedirs(path)

def box_area(xmin, ymin, xmax, ymax):
	return (float(xmax) - float(xmin)) * (float(ymax) - float(ymin))

def mask_img(box):
	xmin, ymin, xmax, ymax = box
	satified = False
	while not satified:
		# print xmin, xmax
		mask_xmin, mask_xmax = sorted(np.random.randint(xmin, xmax+1, 2))
		mask_ymin, mask_ymax = sorted(np.random.randint(ymin, ymax+1, 2))
		ratio = box_area(mask_xmin, mask_ymin, mask_xmax, mask_ymax) / \
			box_area(xmin, ymin, xmax, ymax) 
		if ratio >= 0.3 and ratio < 0.7:
			satified = True
	mask = [mask_xmin, mask_ymin, mask_xmax, mask_ymax]
	return mask

def grey_patch(img, annot):
	# for every object
	# random mask grey patch
	prob = 0.7
	boxes = annot['boxes']
	gt_classes = annot['gt_classes']
	# areas = annot['areas']
	mask_areas, mask_boxes = [], []
	for (box, occ) in zip(boxes, occluded):
		if np.random.rand() < prob:
			mask = mask_img(box)
			cv2.rectangle(img, (mask[0], mask[1]), (mask[2], mask[3]), (104,117,123), -1)
		else:
			mask = [0,0,0,0]
		mask_areas.append(box_area(mask[0], mask[1], mask[2], mask[3]))
		mask_boxes.append(mask)
	return mask_areas, mask_boxes
	# return masked image

if __name__ == '__main__':

	random.seed(100)
	# kitti_dir = '/fldata/dataset/coco/training'
	
	save_dir = '/fldata/dataset/coco/mask/train'
	# train_dir_0 = os.path.join(save_dir, 'train/0')
	train_dir_1 = os.path.join(save_dir, '1')
	# test_dir_0 = os.path.join(save_dir, 'test/0')
	# test_dir_1 = os.path.join(save_dir, 'test/1')
	# create_dir(train_dir_0)
	create_dir(train_dir_1)
	# create_dir(test_dir_0)
	# create_dir(test_dir_1)
	
	# new_annot_dir = os.path.join(save_dir, 'masked_annotations')
	# create_dir(new_annot_dir)
	
	
	coco = my_coco(img_dir, annot_dir)
	# get all images and annotations
	annot_list = kitti._list_annots()
	img_list = kitti._list_imgs()
	
	# iterate every image
	for ix, (img_file, annot_file) in enumerate(zip(img_list, annot_list)):
		if ix % 200 == 0:
			print "processed {} out of {} images".format(ix, len(img_list))
			
		img = cv2.imread(img_file)
		# img_resize_origin = cv2.resize(img, (1000, 600), interpolation=cv2.INTER_CUBIC) 
		# get annotations 
		annot = coco._read_annot(annot_file)
		# generate grey patched image
		mask_areas, mask_boxes = grey_patch(img, annot)

		# origin_save_file = os.path.join(train_dir_0, os.path.basename(img_file))
		save_file = os.path.join(train_dir_1, os.path.basename(img_file))
			
		# kitti._modify_annot(annot_file, mask_areas, mask_boxes, new_annot_dir)
		
		# annot_mv_file = os.path.join(annot_mv_dir, os.path.basename(annot_file))
		# shutil.copyfile(annot_file, annot_mv_file)
		# cv2.imwrite(origin_save_file, img_resize_origin)
		# shutil.copyfile(img_file, origin_save_file)
		# img = cv2.resize(img, (1000, 600), interpolation=cv2.INTER_CUBIC)
		cv2.imwrite(save_file, img)
