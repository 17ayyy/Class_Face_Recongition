# -*- coding: UTF-8 -*-
"""
*@ description: 一些功能中间处理函数
*@ name:	util.py
*@ author:  17_ayyy
*@ time:	2024/11/22 11:07
"""

import cv2
import re
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def extract_name(filename):
    # 使用正则表达式匹配姓名部分
    match = re.match(r"([^\d]+)", filename)
    if match:
        # 返回匹配到的姓名部分
        return match.group(1).strip()
    else:
        # 如果没有匹配到，返回None或者抛出异常
        return None
    
def cv2AddChineseText(img, text, position, textColor=(0, 255, 0), textSize=30):
    
    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text(position, text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

def save_tags_faces(save_path, faces, tags):
    np.savez(save_path, faces=faces, tags=tags)