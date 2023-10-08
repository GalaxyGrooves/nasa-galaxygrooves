import cv2
import numpy as np

rgb_array = cv2.imread('image.png')

height, width, _ = rgb_array.shape
square_size = 10

r_vals = []
g_vals = []
b_vals = []

for i in range(0, height, square_size):
    for j in range(0, width, square_size):
        block_height = min(square_size, height - i)
        block_width = min(square_size, width - j)
        block = rgb_array[i:i + block_height, j:j + block_width]
        r = np.mean(block[:, :, 0])
        g = np.mean(block[:, :, 1])
        b = np.mean(block[:, :, 2])

        r_vals.append(r)
        g_vals.append(g)
        b_vals.append(b)

average_rgb = []
for val in zip(r_vals, b_vals, g_vals):
    average_rgb.append(val)

np_average_rgb = np.array(average_rgb)

# if __name__ == '__main__':
#     manager = multiprocessing.Manager()
#     with multiprocessing.Pool(
#         processes=8,
#     ) as pool:
#         with open('image_folder', 'r') as f:
#             images = f.read()
#         image_folder_lst = []
#         for image in images:
#             image_folder_lst.append(image)
#         results = pool.map(main, images)
#
#     length = results[2]
#     pitch = results[0]
#     volume = results[3]
#
#     for val in zip(length, pitch, volume):
#         print(val)