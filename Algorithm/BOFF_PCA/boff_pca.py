# -*- coding: UTF-8 -*-
"""
*@ description: Boff_pca 人脸识别算法
*@ name:	Boff_pca.py
*@ author: dengbozfan
*@ time:	2024/11/29 20:49
"""

import numpy as np
from typing import List,Tuple
import face_recognition
from sklearn.decomposition import PCA
import joblib
import cv2
from utils.util import cv2AddChineseText

class FaceRecognitionError(Exception):
    """自定义异常,用于处理人脸识别出现的错误"""
    pass

def chack_image_type(image):
    """检查结果是否为ndarray类型, 如果不是则抛出异常"""
    if not isinstance(image, np.ndarray):
        raise FaceRecognitionError("请检查输入的数据是否是ndarray类型")

def get_face_encoding_locations(image:np.ndarray,pca_model:PCA) -> Tuple[List[np.ndarray],List[np.ndarray]]:
    """
    description: 获取人脸面部的编码以及人脸的位置
        Args:
            image : 摄像头拍摄的帧图片 np.ndarray
        return: Tuple[]
            face_encoding: 面部编码 List[np.ndarray]
            face_lactions: 人脸位置 List[np.ndarray]
    """
    # 检查是否是 np.ndarray 类型的数据
    try:
        face_encodings = []
        face_locations = []
        chack_image_type(image) # 检查数据类型
    except FaceRecognitionError as typeError:
        # todo : gui设置 弹窗
        print(f"imageTypeError:{typeError}")
        print(f"当前输入的数据类型为:{type(image)},不是我们要求的ndarray类型")
    else: # 如果没有异常, 则执行下面的语句
        try:
            # 获取人脸特征向量 128个 唯一确定
            face_encodings = face_recognition.face_encodings(image)
            # 获取人脸位置
            face_locations = face_recognition.face_locations(image)
            # 对人脸特征进行pca降维
            face_encodings_pca = []
            for face_encoding in face_encodings:
                face_encoding_pca = pca_model.transform(face_encoding.reshape(1,-1))
                face_encodings_pca.append(face_encoding_pca)
        except Exception as e:
            print(e)

    finally: # 执行无论是否有异常都要执行的语句

        return face_encodings,face_locations

def Boff_pca(image:np.ndarray, faces, tags, pca_model:PCA) -> np.ndarray:
    """
    description: BOFF 人脸识别算法
        Args: 
            image: 待识别的图像 
        return: 绘制识别结果后的image
    """
    # 获取面部特征向量 人脸位置
    face_encodings,face_locations = get_face_encoding_locations(image,pca_model)
    # 进行人脸识别
    for i in range(len(face_encodings)):
        # 面部编码匹配 使用两个向量的内积作为相似度度量,设置阈值
        faceCompare = face_recognition.compare_faces(faces,face_encodings[i],tolerance=0.6)
        try:  
            faceIndex = faceCompare.index(True)
        except ValueError as Ve:
            print("未找到相匹配的人脸! 无法识别!")
        else:
            # 获取边框位置
            top, right, bottom, left = face_locations[i]
            # 获取识别结果对应姓名
            tag = tags[faceIndex]
            # 进行相关绘制
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
            # 添加文本
            image = cv2AddChineseText(image, tag, (left, bottom+25), (0, 255, 0), 30)

    return image

if __name__ == '__main__':
    
    test_four_face_image_path = "..\\..\\images\\test_images\\image_four_face.jpg" # 四个人脸的数据

    pca_model_path = '..\\..\\model\\pca.joblib'
    pca = joblib.load(pca_model_path)

    # 异常测试
    # ...

    # 正常测试
    test_image_four_face = face_recognition.load_image_file(test_four_face_image_path)
    face_encodings,face_locations = get_face_encoding_locations(test_image_four_face,pca_model=pca)