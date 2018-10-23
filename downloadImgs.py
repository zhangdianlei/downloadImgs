# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/22 10:50
@python version: 

"""
import requests

imgsFile = "imgs.dat"

with open(imgsFile, "r+", encoding="utf-8") as f:
    lines = f.readlines()

    for index, line in enumerate(lines):
        line = line.strip('\n')

        if line == "":
            continue

        imgUrl = "http://apps.99wed.com/360app/barcode/barcode.php?codebar=BCGean13&resolution=2&thickness=30&text=" + line
        img = requests.get(imgUrl)
        writeFile = "result/" + line + ".jpg"
        w = open(writeFile, "ab")
        w.write(img.content)
        w.flush()
        w.close()

        if index % 500 == 0:
            print("index:", index)

    f.close()
