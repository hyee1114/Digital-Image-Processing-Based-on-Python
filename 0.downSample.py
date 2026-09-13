def downSample(img,scale):
    num = int (1 // scale)
    m,n = img.shape
    mm = int (m * scale)
    nn = int (n * scale)
    img1 = np.zeros((mm,nn),np.uint8)
    j = 0
    for i in range (0,m,num):
        img1[j,...] = img[i,range(0,n,num)]
        j += 1
    return img1.copy()

import numpy as np

# 调用示例
if __name__ == "__main__":
    test_img = np.random.randint(0 , 255 , (200, 200), dtype=np.uint8)  # 创建一个随机图像
    res_img = downSample(test_img, 0.5)
    print("原图shape：", test_img.shape)
    print("下采样后shape：", res_img.shape)