import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

img = cv2.imread("noise.png", 0)
h, w = img.shape

yy, xx = np.meshgrid(np.linspace(0, h - 1, h),
                     np.linspace(0, w - 1, w),
                     indexing="ij")

freq = 0.11
theta = np.pi / 6
period_noise = 35 * np.sin(2 * np.pi * freq * (xx * np.cos(theta) + yy * np.sin(theta)))

img_noisy = img + period_noise
img_noisy = np.clip(img_noisy, 0, 255).astype(np.uint8)

fft_2d = np.fft.fft2(img_noisy)
fft_shift = np.fft.fftshift(fft_2d)
mag_spectrum = np.log(1 + np.abs(fft_shift))

cx = w // 2
cy = h // 2

grid_y, grid_x = np.ogrid[:h, :w]
dist_center = np.sqrt((grid_x - cx)**2 + (grid_y - cy)**2)
mask = dist_center <= 30
spec_tmp = mag_spectrum.copy()
spec_tmp[mask] = 0

peak_list = []
for _ in range(2):
    pos = np.unravel_index(np.argmax(spec_tmp), (h, w))
    py, px = pos
    peak_list.append((px, py))
    dist_p = np.sqrt((grid_x - px)**2 + (grid_y - py)**2)
    spec_tmp[dist_p <= 14] = 0

plt.figure(figsize=(13, 6))
plt.subplot(121)
plt.imshow(img_noisy, cmap="gray")
plt.title("image with periodic noise added")
plt.axis("off")

ax2 = plt.subplot(122)
ax2.imshow(mag_spectrum, cmap="gray")
plt.title("magnitude spectrum, automatically mark noise peaks")
for xp, yp in peak_list:
    cir = Circle((xp, yp), radius=10, color="red", fill=False, lw=2)
    ax2.add_patch(cir)

plt.axis("off")
plt.tight_layout()
plt.show()

print("检测得到共轭噪声频点坐标(x,y):")
print(peak_list)
