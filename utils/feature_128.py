import face_recognition
import cv2

# 加载图像
image_path = 'images/chump.jpg'
image = face_recognition.load_image_file(image_path)

# 使用face_recognition提取128个人脸特征点
face_landmarks_list = face_recognition.face_landmarks(image)
face_landmarks = face_landmarks_list[0]  # 假设图像中只有一个人脸

# 将图像转换为OpenCV格式
image_cv = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# 创建指定大小的窗口
cv2.namedWindow('Face Landmarks', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Face Landmarks', 640, 480)

# 绘制128个人脸关键特征点
index = 1
for facial_feature_key in face_landmarks:
    for facial_feature in face_landmarks[facial_feature_key]:
        cv2.circle(image_cv, (facial_feature[0], facial_feature[1]), 10, (0, 0, 255), -1)
        cv2.putText(image_cv, str(index), (facial_feature[0], facial_feature[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        index += 1

# 显示绘制特征点后的图像
cv2.imshow('Face Landmarks', image_cv)
cv2.waitKey(0)

# 释放所有窗口
cv2.destroyAllWindows()