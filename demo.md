# Demo - python
* 内网地址：`172.18.141.232`
* 外网地址：`121.196.105.210`

## 数据共享

`docker run -v /workspace/images:/workspace/images ...`

## REPOSITORYs
```
# docker images
REPOSITORY                                               TAG        IMAGE ID       CREATED          SIZE
flystarhe/cicba                                          bce        1f41691ef6b1   31 minutes ago   2.79GB
flystarhe/cicba                                          mmdet      f27e45596ba8   38 minutes ago   8.91GB
registry.cn-hangzhou.aliyuncs.com/flystarhe/containers   mmdet2.7   5e0b65edc821   4 days ago       8.37GB
continuumio/anaconda3                                    2020.11    5e5dd010ead8   4 weeks ago      2.71GB
```

## CONTAINERs
```
# docker ps -a
CONTAINER ID   IMAGE                   COMMAND                  CREATED          STATUS          PORTS                    NAMES
c9866ff2f9da   flystarhe/cicba:bce     "/bin/bash docker/en…"   10 minutes ago   Up 10 minutes   0.0.0.0:7000->9000/tcp   test
4d09856a4da9   flystarhe/cicba:mmdet   "/bin/bash docker/en…"   10 minutes ago   Up 10 minutes   0.0.0.0:7005->9000/tcp   detection
ba1f3b5b3858   flystarhe/cicba:bce     "/bin/bash docker/en…"   11 minutes ago   Up 11 minutes   0.0.0.0:7004->9000/tcp   news_summary
1d0b5373d672   flystarhe/cicba:bce     "/bin/bash docker/en…"   11 minutes ago   Up 11 minutes   0.0.0.0:7003->9000/tcp   dehaze
c5757bddbc6c   flystarhe/cicba:bce     "/bin/bash docker/en…"   11 minutes ago   Up 11 minutes   0.0.0.0:7002->9000/tcp   idcard
eeaad415896d   flystarhe/cicba:bce     "/bin/bash docker/en…"   11 minutes ago   Up 11 minutes   0.0.0.0:7001->9000/tcp   bankcard
```

>为了节约显存，目标检测与实例分割都封装在[http://121.196.105.210:7005/detection](http://121.196.105.210:7005/detection)



```python
import requests

vals = {"image_path": "/workspace/images/demo/bankcard_01.jpg"}
url = "http://121.196.105.210:7001/bankcard"
response = requests.post(url, data=vals)
print(response.json())
```

    {'status': 0, 'data': {'valid_date': '07/22', 'bank_card_number': '6225 9700 7000 3000', 'bank_name': '中国工商银行', 'bank_card_type': 2}}



```python
import requests

vals = {"image_path": "/workspace/images/demo/detection_01.jpg", "score_thr": 0.5, "mode": "det"}
url = "http://121.196.105.210:7005/detection"
response = requests.post(url, data=vals)
print(response.json())
```

    {'status': 0, 'data': {'bbox': [{'xyxy': [1189.452392578125, 656.8873291015625, 1269.86572265625, 705.4522705078125], 'label': 'car', 'score': 0.9974004030227661}, {'xyxy': [1364.575927734375, 715.0731201171875, 1497.0838623046875, 780.3200073242188], 'label': 'car', 'score': 0.9940137267112732}, {'xyxy': [1024.2767333984375, 582.6420288085938, 1067.1143798828125, 620.1596069335938], 'label': 'car', 'score': 0.9875046610832214}, {'xyxy': [237.01031494140625, 605.8427124023438, 569.0455322265625, 919.6438598632812], 'label': 'truck', 'score': 0.9942713975906372}]}}



```python
import requests

vals = {"image_path": "/workspace/images/demo/detection_01.jpg", "score_thr": 0.5, "mode": "seg"}
url = "http://121.196.105.210:7005/detection"
response = requests.post(url, data=vals)
print(response.json())
```

    {'status': 0, 'data': {'bbox': [{'xyxy': [1189.452392578125, 656.8873291015625, 1269.86572265625, 705.4522705078125], 'label': 'car', 'score': 0.9974004030227661}, {'xyxy': [1364.575927734375, 715.0731201171875, 1497.0838623046875, 780.3200073242188], 'label': 'car', 'score': 0.9940137267112732}, {'xyxy': [1024.2767333984375, 582.6420288085938, 1067.1143798828125, 620.1596069335938], 'label': 'car', 'score': 0.9875046610832214}, {'xyxy': [237.01031494140625, 605.8427124023438, 569.0455322265625, 919.6438598632812], 'label': 'truck', 'score': 0.9942713975906372}], 'mask': [[[[1216, 658], [1215, 659], [1210, 659], [1209, 660], [1207, 660], [1205, 662], [1204, 662], [1203, 663], [1202, 663], [1200, 665], [1199, 665], [1193, 671], [1193, 672], [1192, 673], [1192, 689], [1195, 692], [1196, 692], [1197, 693], [1198, 693], [1199, 694], [1200, 694], [1201, 695], [1202, 695], [1203, 696], [1204, 696], [1205, 697], [1206, 697], [1207, 698], [1208, 698], [1210, 700], [1211, 700], [1212, 701], [1214, 701], [1215, 702], [1245, 702], [1246, 703], [1252, 703], [1253, 704], [1265, 704], [1266, 703], [1266, 701], [1267, 700], [1267, 698], [1268, 697], [1268, 680], [1267, 679], [1267, 678], [1266, 677], [1266, 676], [1264, 674], [1264, 673], [1263, 672], [1262, 672], [1258, 668], [1258, 666], [1253, 661], [1252, 661], [1251, 660], [1247, 660], [1246, 659], [1239, 659], [1238, 658]]], [[[1409, 717], [1408, 718], [1404, 718], [1403, 719], [1401, 719], [1400, 720], [1399, 720], [1396, 723], [1395, 723], [1394, 724], [1393, 724], [1392, 725], [1391, 725], [1390, 726], [1389, 726], [1388, 727], [1387, 727], [1386, 728], [1385, 728], [1384, 729], [1382, 729], [1381, 730], [1380, 730], [1379, 731], [1377, 731], [1376, 732], [1375, 732], [1374, 733], [1373, 733], [1370, 736], [1370, 737], [1369, 738], [1369, 746], [1368, 747], [1368, 749], [1367, 750], [1367, 752], [1366, 753], [1367, 754], [1367, 755], [1368, 756], [1368, 757], [1370, 759], [1371, 759], [1372, 760], [1375, 760], [1376, 761], [1381, 761], [1382, 762], [1387, 762], [1388, 763], [1394, 763], [1395, 764], [1397, 764], [1398, 765], [1400, 765], [1401, 766], [1402, 766], [1403, 767], [1405, 767], [1406, 768], [1408, 768], [1409, 769], [1410, 769], [1411, 770], [1412, 770], [1413, 771], [1414, 771], [1416, 773], [1417, 773], [1418, 774], [1419, 774], [1420, 775], [1421, 775], [1422, 776], [1427, 776], [1428, 777], [1446, 777], [1447, 776], [1450, 776], [1451, 775], [1454, 775], [1455, 774], [1459, 774], [1460, 775], [1467, 775], [1468, 776], [1471, 776], [1473, 778], [1476, 778], [1477, 779], [1482, 779], [1483, 778], [1484, 778], [1487, 775], [1487, 774], [1488, 773], [1488, 772], [1491, 769], [1491, 768], [1492, 767], [1492, 766], [1493, 765], [1493, 764], [1495, 762], [1495, 747], [1494, 746], [1494, 744], [1493, 743], [1493, 741], [1492, 740], [1492, 739], [1491, 738], [1491, 737], [1487, 733], [1487, 732], [1485, 730], [1484, 730], [1477, 723], [1476, 723], [1475, 722], [1474, 722], [1473, 721], [1472, 721], [1471, 720], [1468, 720], [1467, 719], [1462, 719], [1461, 718], [1446, 718], [1445, 717]]], [[[1034, 584], [1028, 590], [1028, 591], [1027, 592], [1027, 593], [1026, 594], [1026, 599], [1025, 600], [1025, 616], [1026, 617], [1027, 616], [1034, 616], [1035, 617], [1036, 616], [1042, 616], [1043, 617], [1058, 617], [1059, 618], [1064, 618], [1064, 617], [1065, 616], [1065, 598], [1064, 597], [1064, 594], [1063, 593], [1063, 592], [1060, 589], [1060, 588], [1059, 587], [1058, 587], [1057, 586], [1056, 586], [1055, 585], [1049, 585], [1048, 584]]], [[[471, 607], [470, 608], [460, 608], [459, 609], [455, 609], [454, 610], [452, 610], [451, 611], [450, 611], [449, 612], [448, 612], [447, 613], [446, 613], [445, 614], [443, 614], [442, 615], [438, 615], [437, 616], [431, 616], [430, 617], [425, 617], [424, 618], [420, 618], [419, 619], [417, 619], [416, 620], [414, 620], [412, 622], [411, 622], [410, 623], [409, 623], [407, 625], [405, 625], [404, 626], [402, 626], [401, 627], [399, 627], [398, 628], [394, 628], [393, 629], [389, 629], [388, 630], [385, 630], [384, 631], [382, 631], [381, 632], [380, 632], [377, 635], [376, 635], [375, 636], [374, 636], [373, 637], [371, 637], [370, 638], [367, 638], [366, 639], [362, 639], [361, 640], [357, 640], [356, 641], [354, 641], [353, 642], [351, 642], [350, 643], [349, 643], [348, 644], [347, 644], [345, 646], [344, 646], [342, 648], [340, 648], [339, 649], [337, 649], [336, 650], [333, 650], [332, 651], [329, 651], [328, 652], [326, 652], [325, 653], [322, 653], [321, 654], [319, 654], [318, 655], [317, 655], [316, 656], [315, 656], [314, 657], [313, 657], [312, 658], [311, 658], [310, 659], [308, 659], [307, 660], [305, 660], [304, 661], [302, 661], [301, 662], [300, 662], [299, 663], [298, 663], [297, 664], [296, 664], [294, 666], [293, 666], [290, 669], [290, 670], [287, 673], [287, 674], [286, 675], [286, 676], [285, 677], [285, 680], [284, 681], [284, 684], [283, 685], [283, 688], [282, 689], [282, 691], [281, 692], [281, 693], [280, 694], [280, 695], [278, 697], [278, 698], [277, 699], [277, 700], [276, 701], [276, 702], [275, 703], [275, 704], [274, 705], [274, 707], [273, 708], [273, 710], [272, 711], [272, 712], [271, 713], [271, 714], [267, 718], [266, 718], [262, 722], [262, 723], [261, 724], [261, 725], [260, 726], [260, 727], [253, 734], [253, 735], [251, 737], [251, 738], [249, 740], [249, 741], [248, 742], [248, 743], [247, 744], [247, 746], [246, 747], [246, 748], [244, 750], [244, 751], [242, 753], [242, 754], [241, 755], [241, 756], [240, 757], [240, 760], [239, 761], [239, 767], [238, 768], [238, 825], [239, 826], [239, 847], [240, 848], [240, 857], [241, 858], [241, 866], [242, 867], [242, 875], [243, 876], [243, 881], [244, 882], [244, 885], [245, 886], [245, 889], [246, 890], [246, 893], [247, 894], [247, 896], [248, 897], [248, 899], [249, 900], [249, 902], [250, 903], [250, 904], [255, 909], [256, 909], [257, 910], [258, 910], [260, 912], [261, 912], [262, 913], [263, 913], [264, 914], [265, 914], [266, 915], [270, 915], [271, 916], [298, 916], [299, 915], [324, 915], [325, 916], [344, 916], [345, 917], [362, 917], [363, 916], [372, 916], [373, 915], [376, 915], [377, 914], [379, 914], [380, 913], [381, 913], [382, 912], [383, 912], [384, 911], [386, 911], [387, 910], [388, 910], [389, 909], [390, 909], [391, 908], [392, 908], [393, 907], [395, 907], [396, 906], [397, 906], [407, 896], [408, 896], [410, 894], [411, 894], [413, 892], [413, 891], [419, 885], [420, 885], [422, 883], [423, 883], [432, 874], [433, 874], [434, 873], [435, 873], [440, 868], [441, 868], [444, 865], [445, 865], [447, 863], [448, 863], [454, 857], [455, 857], [469, 843], [470, 843], [474, 839], [474, 838], [480, 832], [481, 832], [483, 830], [484, 830], [487, 827], [488, 827], [491, 824], [492, 824], [497, 819], [498, 819], [500, 817], [501, 817], [503, 815], [504, 815], [506, 813], [507, 813], [512, 808], [513, 808], [514, 807], [515, 807], [517, 805], [518, 805], [523, 800], [524, 800], [527, 797], [528, 797], [530, 795], [531, 795], [556, 770], [556, 769], [557, 768], [557, 767], [558, 766], [558, 764], [559, 763], [559, 762], [560, 761], [560, 760], [561, 759], [561, 758], [562, 757], [562, 756], [563, 755], [563, 753], [564, 752], [564, 749], [565, 748], [565, 718], [564, 717], [564, 705], [565, 704], [565, 670], [566, 669], [566, 664], [565, 663], [565, 647], [566, 646], [566, 644], [565, 643], [565, 636], [564, 635], [564, 631], [563, 630], [563, 627], [562, 626], [562, 625], [561, 624], [561, 622], [558, 619], [558, 618], [552, 612], [551, 612], [550, 611], [549, 611], [548, 610], [546, 610], [545, 609], [543, 609], [542, 608], [538, 608], [537, 607]]]]}}

