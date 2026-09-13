#生成指定图像
import numpy as np
import matplotlib.pyplot as plt
def generate_img():
    img = np.zeros((512, 512))
    img[156:356, 156:356] = 255
    return img

#示例
img1 = generate_img()
plt.imshow(img1, cmap='gray')
plt.show() #可视化图片