#!/usr/bin/env python
# coding: utf-8

import yaml
import sys

hyps=dict(
    lr0= float(sys.argv[1]),
    lrf= 0.01,
    momentum = float(sys.argv[2]),
    weight_decay = float(sys.argv[3]),
    warmup_epochs = 3.0,
    warmup_momentum = 0.8,
    warmup_bias_lr= 0.1,
    box= 0.05,
    cls= 0.5,
    cls_pw= 1.0,
    obj= 1.0,
    obj_pw= 1.0,
    iou_t= 0.2,
    anchor_t= 4.0,
    fl_gamma= 0.0,
    hsv_h= 0.015,
    hsv_s= 0.7,
    hsv_v= 0.4,
    degrees= 0.0,
    translate= 0.1,
    scale= 0.5,
    shear= 0.0,
    perspective= 0.0,
    flipud= 0.0,
    fliplr= 0.5,
    mosaic= 1,
    mixup= 0.0,
    copy_paste= 0.0
)

with open('/home/simona/SAMPLE/GPU/GabijosTyrimas/yolov5/data/hyps/hyp.Auto.yaml', 'w') as outfile:
    yaml.dump(hyps, outfile, sort_keys=False)

