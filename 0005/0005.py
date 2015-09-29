#!/usr/bin/python
# -*- coding: utf-8 -*-
# by JeffMa at http://devework.com/

#第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率(1136x640)的大小。

import os, fnmatch
from PIL import Image

# 裁剪图片函数
def Resize_img(file_name):
    img = Image.open(file_name)
    # 目标裁剪大小
    resolution = (200,100)
    scaler = Image.ANTIALIAS
    new_image = img.resize(resolution,scaler)
    # 重命名
    new_file_name = file_name.split('.')[0]+'_new.'+file_name.split('.')[-1]
    print new_file_name
    new_image.save(new_file_name)


# 遍历目标目录下的相关文件
def Find_file(root='.', recurse=True, pattern='*'):
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                yield os.path.join(path, name)
        if not recurse:
            break

if __name__ == '__main__':
    recurse = True
    for files in Find_file("photos", recurse, '*.jpg'):
        Resize_img(files)
