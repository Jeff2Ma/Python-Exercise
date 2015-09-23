#!/usr/bin/python
# -*- coding: utf-8 -*-

# by JeffMa
# 题目：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

from PIL import Image, ImageFont, ImageDraw
img = Image.open(r'avatar.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(r'font.ttf', 20)
draw.text((65, -4), '6', (255, 0, 0), font=font)
img.save('avater-edit.jpg')
