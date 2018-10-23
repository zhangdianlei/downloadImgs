# encoding: utf-8
"""
@author: Dianlei Zhang
@contact: dianlei.zhang@qq.com

@time: 2018/10/22 11:22
@python version: 

"""

codeFile = "code.dat"
imgsFile = "imgs.dat"

with open("file.dat", 'r+', encoding="utf-8") as f:
    lines = f.readlines()

    for index, line in enumerate(lines):
        line = line.strip('\n')

        if line == "":
            continue

        if index % 500 == 0:
            print("index:", index)
