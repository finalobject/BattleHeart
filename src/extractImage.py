# -*- coding:utf-8 -*- 
path = "../res/video/a.flv"
import numpy as np
import cv2
cap = cv2.VideoCapture(path)                         # 创建一个VideoCapture对象
while(True):
	ret, frame = cap.read()                       # 一帧一帧读取视频
	cv2.imshow('frame',frame)                      # 显示结果
	if cv2.waitKey(1) & 0xFF == ord('q'):         # 按q停止
		break
cap.release()
cv2.destroyAllWindows()