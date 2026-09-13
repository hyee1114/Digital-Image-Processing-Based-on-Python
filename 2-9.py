#生成图2-33的直方图
import numpy as np
import matplotlib.pyplot as plt
def hist(img):
    m,n = img.shape
    h = np.zeros(2) 
    for i in range (0,m):
        for j in range (0,n):
            if img[i,j] == 0:
                h[0] += 1
            else:
                h[1] += 1
    return h


#示例
img1 = np.array([[1,1,1,1,1],[1,1,1,0,1],[1,1,0,0,1],[1,0,1,1,1],[1,1,1,1,1]])
h1 = hist(img1).astype(int)
print("图像1为：")
print(img1)
print("图像1的直方图为：", h1)

# 绘图
plt.figure(figsize=(8,3))
plt.subplot(1,2,1)
plt.imshow(img1, cmap='gray')
plt.title("img1")

plt.subplot(1,2,2)
plt.bar([0,1], h1, width=0.5)
plt.xticks([0, 1])       # 强制x轴只显示 0 和 1 两个刻度！
plt.title("histogram of img1")
plt.xlabel("gray value")
plt.ylabel("pixel number")
plt.tight_layout()
plt.show()