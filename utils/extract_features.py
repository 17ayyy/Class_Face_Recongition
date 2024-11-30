# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-
"""
*@ description: 基于face_recognition提取人脸特征
*@ name:	extract_features.py
*@ author:  17_ayyy
*@ time:	2024/11/28 16:38
"""

import face_recognition
import os
from tqdm import tqdm
import numpy as np
from util import extract_name
from util import save_tags_faces
from sklearn.decomposition import PCA
import joblib

def train(train_images_path, save_path_npz, save_path_pca, is_save=True):
    """
    description: 获取所有同学面部编码
        Args: 
            images_path : 训练图片路径
        return:
            faces : 人脸面部特征编码存储列表
            tags : labels
            使用numpy的npz文件进行存储
            使用joblib存储pca模型
    """
    
    train_images = os.listdir(train_images_path)
    print(f"该文件夹共有{len(train_images)}个训练数据")

    tags = []
    faces = []

    for image_filename in tqdm(train_images):
        image_path = os.path.join(train_images_path, image_filename)
        image = face_recognition.load_image_file(image_path)
        # 获取图像中所有面部编码
        face = face_recognition.face_encodings(image)[0]
        # 获取姓名
        name = extract_name(image_filename)
        faces = faces + [face]
        tags = tags + [name]

    print("=="*20)
    print(tags)
    faces_array = np.array(faces)
    tags_array = np.array(tags)
    tags_labelEncoded_array = np.array(labelEncoding(tags)) # 编码量化
    
    # if is_save:
    #     save_tags_faces(save_path, faces=faces_array, tags=tags_array)
    #     print("保存完成")

    # 创建PCA对象，设置降维后的主成分个数
    pca = PCA(n_components=30,svd_solver='auto')
    # 对数据进行训练
    pca.fit(faces)
    # 存储模型
    joblib.dump(pca, save_path_pca)
    # 转化数据
    faces_r = pca.transform(faces)

    np.savez(save_path_npz,faces=faces_array,faces_r=faces_r,
             tags=tags_array,tags_labelEncoded=tags_labelEncoded_array)

    print("++!训练完毕!++")

def labelEncoding(tags):
    """
    description: 对tag进行编码量化
        Args: 
            faces: 面部编码特征向量
            tags : 对应的标签/姓名 
        return: tags
    """
    train_images = os.listdir(train_images_path)
    labels = {}
    for idx, label in enumerate(train_images):
        feature = extract_name(label)
        labels[feature] = idx
    tag_encoding = []
    for tag in tags:
        tag_encoding.append(labels[tag])

    print(tag_encoding)

    return tag_encoding

if __name__ == '__main__':

    train_images_path = '..\\images\\train_images'
    save_path_npz = '..\\model\\tags_faces.npz'
    save_path_pca = '..\\model\\pca.joblib'
    train(train_images_path, save_path_npz, save_path_pca)

    with np.load(save_path_npz) as sa:
        faces = sa["faces"]
        faces_r = sa["faces_r"]
        tags = sa["tags"]
        tags_labelEncoded = sa["tags_labelEncoded"]
    
    print("=="*20)
    print(faces.shape)
    print(faces_r.shape)
    print("=="*20)
    print(tags)
    print(tags_labelEncoded)

