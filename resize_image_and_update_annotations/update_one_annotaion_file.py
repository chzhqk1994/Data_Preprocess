import xml.etree.ElementTree as ET

resize_width = 300
resize_height = 300

xml_label_path = '/home/qisens/new_modify_label.xml'


def xml_label_resize(label_path):
    tree = ET.parse(label_path)
    root = tree.getroot()

    origin_width = 0
    origin_height = 0

    # Get image size from XML file
    for size in root.findall('size'):
        origin_width = size.find('width').text
        origin_height = size.find('height').text
        print('width : ', origin_width)
        print('height : ', origin_height)
        print()

    # XML 파일의 image size 를 resize 값 으로 update
    for width in root.iter('width'):
        width.text = str(resize_width)

    for height in root.iter('height'):
        height.text = str(resize_height)

    # width, height 의 ratio 계산
    width_ratio = resize_width / int(origin_width)
    height_ratio = resize_height / int(origin_height)
    print('width ratio : ', width_ratio)
    print('height ratio : ', height_ratio)
    print()

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

    print('xmin_list : ', xmin_list)
    print('ymin_list : ', ymin_list)
    print('xmax_list : ', xmax_list)
    print('ymax_list : ', ymax_list)


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

    tree.write(xml_label_path)


xml_label_resize(xml_label_path)
