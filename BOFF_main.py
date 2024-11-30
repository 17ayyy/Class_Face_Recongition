import face_recognition
import numpy as np
import time
import cv2
from utils.util import cv2AddChineseText
save_path = "model/tags_faces.npz"

# 载入数据
with np.load(save_path) as data:
    faces = data["faces"]
    tags = data["tags"]

cap = cv2.VideoCapture(0)
# 设置摄像头的长宽参数
width = 640
height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

frame_count = 0

while True:

    ret, frame = cap.read()  # 获取一帧图片
    start_time = time.time()  # 计时
    # 获取面部编码
    names = face_recognition.face_encodings(frame)
    # 定位图中所有人脸
    face_locations = face_recognition.face_locations(frame)

    for i in range(len(names)):
        # 面部编码匹配 使用两个向量的内积作为相似度度量,设置阈值
        faceCompare = face_recognition.compare_faces(faces,names[i],tolerance=0.5)
        try:
            faceIndex = faceCompare.index(True)
            # 获取边框位置
            top, right, bottom, left = face_locations[i]
            print((top, right, bottom, left))
            # 进行相关绘制
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            # 添加文本
            frame = cv2AddChineseText(frame, tags[faceIndex], (left, bottom+25), (0, 255, 0), 30)
            frame = cv2AddChineseText(frame, f"花费时间:{time.time() - start_time:.2f}", (10,30), (0, 255, 0), 30)
            frame = cv2AddChineseText(frame, f"FPS: {frame_count / (time.time() - start_time):.2f}", (10,60), (0, 255, 0), 30)

        except Exception as e:
            print("未识别出")
            continue

    frame_count += 1
    # 展示图像
    cv2.imshow("Face_reco", frame)
    # 退出设置
    key = cv2.waitKey(1) & 0xff
    if key == ord("q"):
        break

cap.release()  # 释放摄像头资源
cv2.destroyAllWindows()