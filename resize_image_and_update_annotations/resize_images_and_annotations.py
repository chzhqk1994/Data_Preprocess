import os
from PIL import Image, ImageFile
import xml.etree.ElementTree as ET

ImageFile.LOAD_TRUNCATED_IMAGES = True

resize_width = 300
resize_height = 300

root_path = '/home/qisens/dataset_backup/300x300/all_bmt_compcar_major_maker_training/'

# root_path/
#         ㄴ images/
#         ㄴ annotations/ (xml files)

def xml_label_resize(label_path):
    origin_width = 0
    origin_height = 0
    label_path = label_path + 'annotations/'

    cnt = 0
    for (path, dir, files) in os.walk(label_path):
        for file in files:
            anno_path = os.path.join(path, file)

            tree = ET.parse(anno_path)
            root = tree.getroot()

            # Get image size from XML file
            for size in root.findall('size'):
                origin_width = size.find('width').text
                origin_height = size.find('height').text

            # XML 파일의 image size 를 resize 값 으로 update
            for width in root.iter('width'):
                width.text = str(resize_width)

            for height in root.iter('height'):
                height.text = str(resize_height)

            # width, height 의 ratio 계산
            width_ratio = resize_width / int(origin_width)
            height_ratio = resize_height / int(origin_height)

            # xml annotation 에서 좌표 값 들을 뽑아내어 resize 후 값 들을 저장
            xmin_list = []
            ymin_list = []
            xmax_list = []
            ymax_list = []
            for object in root.findall('object'):
                for bndbox in object.findall('bndbox'):
                    value = bndbox.find('xmin').text
                    xmin_list.append(1 if int(float(value) * width_ratio) == 0 else int(float(value) * width_ratio))

                    value = bndbox.find('ymin').text
                    ymin_list.append(1 if int(float(value) * height_ratio) == 0 else int(float(value) * height_ratio))

                    value = bndbox.find('xmax').text
                    xmax_list.append(int(float(value) * width_ratio))

                    value = bndbox.find('ymax').text
                    ymax_list.append(int(float(value) * height_ratio))

            index = 0
            for xmin in root.iter('xmin'):
                xmin.text = str(xmin_list[index])
                index += 1

            index = 0
            for ymin in root.iter('ymin'):
                ymin.text = str(ymin_list[index])
                index += 1

            index = 0
            for xmax in root.iter('xmax'):
                xmax.text = str(xmax_list[index])
                index += 1

            index = 0
            for ymax in root.iter('ymax'):
                ymax.text = str(ymax_list[index])
                index += 1

            tree.write(anno_path)

            cnt += 1
            print('{}   {}'.format(cnt, anno_path))


def resize_image_annotation_edited(path):
    cnt = 0
    path = path + 'images/'

    for (path, dir, files) in os.walk(path):
        for file in files:
            img_path = os.path.join(path, file)
            img = Image.open(img_path)

            img = img.resize((resize_width, resize_height), Image.ANTIALIAS)
            img.save(img_path)

            cnt += 1
            print('{}   {}'.format(cnt, img_path))


# resize_image_annotation_edited(root_path)
xml_label_resize(root_path)
