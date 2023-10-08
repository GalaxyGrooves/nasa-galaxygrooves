import cv2
import numpy as np
import multiprocessing
# from multiprocessing import Pool

rgb_array = cv2.imread('image.png')
np_rgb_array = np.array(rgb_array)
length = np_rgb_array.size
width = np_rgb_array[0].size
average_array = []
square_sides = 10
r_vals = []
g_vals = []
b_vals = []
for i in range(length):
    for j in range(width):
        r = rgb_array[i][j][0]
        r_vals.append(r)
        g = rgb_array[i][j][1]
        g_vals.append(g)
        b = rgb_array[i][j][2]
        b_vals.append(b)

for i in range(0, len(r_vals), 10):
    chunk = r_vals[i:i + 10]
    average = sum(chunk) / len(chunk)

for i in range(0, len(b_vals), 10):
    chunk = r_vals[i:i + 10]
    average = sum(chunk) / len(chunk)

for i in range(0, len(g_vals), 10):
    chunk = r_vals[i:i + 10]
    average = sum(chunk) / len(chunk)


# print(rgb_array[0][0][0])



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