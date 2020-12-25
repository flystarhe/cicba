import os.path as __osp

__MMDET_PATH = '/usr/src/mmdetection'

_base_ = [
    __osp.join(__MMDET_PATH, 'configs/_base_/models/faster_rcnn_r50_fpn.py'),
    __osp.join(__MMDET_PATH, 'configs/_base_/datasets/coco_detection.py'),
    __osp.join(__MMDET_PATH, 'configs/_base_/schedules/schedule_2x.py'),
    __osp.join(__MMDET_PATH, 'configs/_base_/default_runtime.py'),
]

model = dict(pretrained='torchvision://resnet101', backbone=dict(depth=101))
