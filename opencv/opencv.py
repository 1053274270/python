import cv2
import numpy as np

# imread()函数读取目标图片和模板
img = cv2.imread(r"C:\Users\Lenovo\Desktop\test.png")
template = cv2.imread(r"C:\Users\Lenovo\Desktop\test1.png", 0) 

#w,h = template.shape[:2]
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.namedWindow('aaa',cv2.WINDOW_NORMAL)
#cv2.imshow('aaa',img)
#cv2.waitKey(0)


#left_top = max_loc  # 左上角
#right_bottom = (left_top[0] + w, left_top[1] + h)  # 右下角
#cv2.rectangle(img, left_top, right_bottom, 255, 2)  # 画出矩形位置
# matchTemplate 函数：在模板和输入图像之间寻找匹配,获得匹配结果图像 
# minMaxLoc 函数：在给定的矩阵中寻找最大和最小值，并给出它们的位置
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)

#bottom_right = (top_left[0] + w, top_left[1] + h)
#cv2.rectangle(img,top_left, bottom_right, 255, 2)

