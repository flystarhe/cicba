# docker
```
docker build -t flystarhe/cicba:bce -f bce .
docker build -t flystarhe/cicba:mmdet -f mmdet .
```

## bankcard (ocr_cards/bankcard - 免费/500次/天 - 200元/万次)
```
docker run -d -p 7001:9001 --ipc=host --name bankcard -v /workspace/images:/workspace/images flystarhe/cicba:bce bankcard 9001 doMFkEYsD3eVKi2O8QuyiPlH wPQAue6Be36Ww6fk9mY6fAFygsdmgl4p
```

## idcard (ocr_cards/idcard - 免费/500次/天 - 200元/万次)
```
docker run -d -p 7002:9001 --ipc=host --name idcard -v /workspace/images:/workspace/images flystarhe/cicba:bce idcard 9001 doMFkEYsD3eVKi2O8QuyiPlH wPQAue6Be36Ww6fk9mY6fAFygsdmgl4p
```

## dehaze (imageprocess/dehaze - 免费/共3000次 - 7元/千次)
```
docker run -d -p 7003:9001 --ipc=host --name dehaze -v /workspace/images:/workspace/images flystarhe/cicba:bce dehaze 9001 SrwxDe8ef0y0QGl617T5FqkF RZWMBGysUcAmukScqiGhhAQtMq28xnT6
```

## news_summary (nlp_apply/news_summary - 免费/共50万次 - 280元/10万次)
```
docker run -d -p 7004:9001 --ipc=host --name news_summary -v /workspace/images:/workspace/images flystarhe/cicba:bce news_summary 9001 9zXDM42tKyYzmOEdIDhO306A dG6RWePPFzGHq4YUYjQtS7U4xV95H3rG
```

## detection (mmdet2/detection - 目标检测/本地gpu)
```
docker run --gpus device=0 -d -p 7005:9001 --ipc=host --name detection -v /workspace/images:/workspace/images flystarhe/cicba:mmdet detection 9001
```

## segmentation (mmdet2/segmentation - 实例分割/本地gpu)
```
docker run --gpus device=0 -d -p 7006:9001 --ipc=host --name segmentation -v /workspace/images:/workspace/images flystarhe/cicba:mmdet segmentation 9001
```
