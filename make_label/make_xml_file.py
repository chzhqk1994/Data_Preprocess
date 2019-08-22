from xml.etree.ElementTree import Element, SubElement
from xml.etree import ElementTree
from xml.dom import minidom
import os
import cv2

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="        ")


label = 'maserati/'
labelnum = 324

dataset_path = '/home/qisens/test_maserati/images/' + label
output_root = '/home/qisens/test_maserati/annotations/'

for root, dirs, files in os.walk(dataset_path, topdown=False):
    print(root)
    if not os.path.exists(output_root + label):
        os.makedirs(output_root + label)

    for file in files:
        print(root + file)

        img = cv2.imread(root + file, cv2.IMREAD_UNCHANGED)
        folder_name = root[33:-1]
        print(img.shape)
        print(file)
        print(folder_name)

        annotation = Element('annotation')

        folder = SubElement(annotation, 'folder')
        folder.text = folder_name

        filename = SubElement(annotation, 'filename')
        filename.text = file

        path = SubElement(annotation, 'path')
        path.text = root + file

        source = SubElement(annotation, 'source')
        database = SubElement(source, 'database')
        database.text = 'Unknown'

        size = SubElement(annotation, 'size')
        width = SubElement(size, 'width')
        width.text = str(img.shape[1])
        height = SubElement(size, 'height')
        height.text = str(img.shape[0])
        depth = SubElement(size, 'depth')
        depth.text = str(3)

        segmented = SubElement(annotation, 'segmented')
        segmented.text = '0'

        object = SubElement(annotation, 'object')
        name = SubElement(object, 'name')
        name.text = str(labelnum)
        pose = SubElement(object, 'pose')
        pose.text = 'Unspecified'
        truncated = SubElement(object, 'truncated')
        truncated.text = '0'
        difficult = SubElement(object, 'difficult')
        difficult.text = '0'

        bndbox = SubElement(object, 'bndbox')
        xmin = SubElement(bndbox, 'xmin')
        xmin.text = '1'
        ymin = SubElement(bndbox, 'ymin')
        ymin.text = '1'
        xmax = SubElement(bndbox, 'xmax')
        xmax.text = str(img.shape[1] - 1)
        ymax = SubElement(bndbox, 'ymax')
        ymax.text = str(img.shape[0] - 1)

        result = prettify(annotation)
        print(result)
        print('\n\n\n')

        # tree = ElementTree.ElementTree()
        # tree._setroot(annotation)
        # tree.write("sample.xml")

        # file[:-4] 는 확장자를 제외한 파일 이름
        f = open(output_root + label + file[:-4] + '.xml', 'w')
        f.write(result)
        f.close()
