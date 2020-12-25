import os.path as __osp

__MMDET_PATH = '/usr/src/mmdetection'

_base_ = [
    __osp.join(__MMDET_PATH, 'configs/_base_/models/mask_rcnn_r50_fpn.py'),
    __osp.join(__MMDET_PATH, 'configs/_base_/datasets/coco_instance.py'),
    __osp.join(__MMDET_PATH, 'configs/_base_/schedules/schedule_2x.py'),
    __osp.join(__MMDET_PATH, 'configs/_base_/default_runtime.py'),
]

model = dict(
    pretrained='open-mmlab://resnext101_32x4d',
    backbone=dict(
        type='ResNeXt',
        depth=101,
        groups=32,
        base_width=4,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=True),
        style='pytorch'))
