#计算图像平均灰度值
def ave_gray(img):
    m,n = img.shape
    sum_gray = np.sum(img)
    ave_gray_value = sum_gray / (m * n)
    return ave_gray_value




#示例
import numpy as np
img1 = np.array([[2,4,5,6],[3,1,5,3],[6,2,2,2]])
print("图像1为：")
print(img1)
print("图像1的平均灰度值为：",ave_gray(img1))