import os
from shutil import copy

dataset_path = './images/'

output_root = './images_output/'
img_output_path = './images_output/images/'
label_output_path = './images_output/annotations/'

make_list = []
file_list = []

if not os.path.exists(img_output_path):
    os.makedirs(img_output_path)
if not os.path.exists(label_output_path):
    os.makedirs(label_output_path)

for root, _, files in os.walk(dataset_path, topdown=False):
    maker = root[9:]
    print(root, files)
    for file in files:
        print('maker : ', root[9:])
        print('file : ', files[0][-3:])

        if file[-3:] == 'xml':
            if not os.path.exists(label_output_path + maker):
                os.makedirs(label_output_path + maker)
            copy(dataset_path + maker + '/' + file, label_output_path + maker)

        elif file[-3:] == 'jpg':
            if not os.path.exists(img_output_path + maker):
                os.makedirs(img_output_path + maker)
            copy(dataset_path + maker + '/' + file, img_output_path + maker)

        else:
            pass
