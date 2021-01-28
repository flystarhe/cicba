# docker
```
docker build -t flystarhe/cicba:bce -f bce .
docker build -t flystarhe/cicba:mmdet -f mmdet .
```

## bankcard (ocr_cards/bankcard - 免费/500次/天 - 200元/万次)
```
docker run -d -p 7001:9000 --ipc=host --name bankcard -v /workspace/images:/workspace/images flystarhe/cicba:bce bankcard 9000 doMFkEYsD3eVKi2O8QuyiPlH wPQAue6Be36Ww6fk9mY6fAFygsdmgl4p
```

## idcard (ocr_cards/idcard - 免费/500次/天 - 200元/万次)
```
docker run -d -p 7002:9000 --ipc=host --name idcard -v /workspace/images:/workspace/images flystarhe/cicba:bce idcard 9000 doMFkEYsD3eVKi2O8QuyiPlH wPQAue6Be36Ww6fk9mY6fAFygsdmgl4p
```

## dehaze (imageprocess/dehaze - 免费/共3000次 - 7元/千次)
```
docker run -d -p 7003:9000 --ipc=host --name dehaze -v /workspace/images:/workspace/images flystarhe/cicba:bce dehaze 9000 SrwxDe8ef0y0QGl617T5FqkF RZWMBGysUcAmukScqiGhhAQtMq28xnT6
```

## news_summary (nlp_apply/news_summary - 免费/共50万次 - 280元/10万次)
```
docker run -d -p 7004:9000 --ipc=host --name news_summary -v /workspace/images:/workspace/images flystarhe/cicba:bce news_summary 9000 9zXDM42tKyYzmOEdIDhO306A dG6RWePPFzGHq4YUYjQtS7U4xV95H3rG
```

## detection (mmdet2/detection - 目标检测/本地gpu)
```
docker run --gpus device=0 -d -p 7005:9000 --ipc=host --name detection -v /workspace/images:/workspace/images flystarhe/cicba:mmdet detection 9000
docker run --gpus device=0 -d -p 8000:9000 --ipc=host --name det_test -v /workspace/images:/workspace/images flystarhe/cicba:mmdet dev
docker run --gpus device=0 -d -p 8001:9000 --ipc=host --name det_faster -v /workspace/images:/workspace/images flystarhe/cicba:mmdet detection 9000 faster_rcnn_x101_32x4d_fpn_2x_coco
docker run --gpus device=0 -d -p 8002:9000 --ipc=host --name det_mask -v /workspace/images:/workspace/images flystarhe/cicba:mmdet detection 9000 mask_rcnn_x101_32x4d_fpn_2x_coco
```

## segmentation (mmdet2/segmentation - 实例分割/本地gpu)
```
docker run --gpus device=0 -d -p 7006:9000 --ipc=host --name segmentation -v /workspace/images:/workspace/images flystarhe/cicba:mmdet segmentation 9000
```

## business (ocr_cards/business - 200次/天免费 - 暂不支持购买)
```
docker run -d -p 7007:9000 --ipc=host --name business -v /workspace/images:/workspace/images flystarhe/cicba:bce business 9000 doMFkEYsD3eVKi2O8QuyiPlH wPQAue6Be36Ww6fk9mY6fAFygsdmgl4p
```
