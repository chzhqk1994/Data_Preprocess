import os
import cv2

label = 'vw/'
labelnum = 324

dataset_path = '/home/qisens/majormakers/image/' + label
output_root = '/home/qisens/majormakers/images_output/'

for root, dirs, files in os.walk(dataset_path, topdown=False):
    print(root)
    if not os.path.exists(output_root + label):
        os.makedirs(output_root + label)

    for file in files:
        print(root + file)

        img = cv2.imread(root + file, cv2.IMREAD_UNCHANGED)
        print(img.shape[0], img.shape[1], img.shape[2])
        print(file)
        print(root[31:-1])
        # make xml file
        f = open(output_root + label + file[:-4] + '.xml', 'w')

        data = '<annotation>\n        ' + '<folder>' + root[31:-1] + '</folder>\n        ' +\
               '<filename>' + file + '</filename>\n        ' +\
               '<path>' + root + file + '</path>\n        ' + '<source>\n        ' +\
               '        <database>' + 'Unknown' + '</database>\n        ' + '</source>\n        ' +\
            '<size>\n' + '                <width>' + str(img.shape[1]) + '</width>\n' + '                <height>' + str(img.shape[0]) + '</height>\n                ' +\
            '<depth>' + str(img.shape[2]) + '</depth>\n' + '        </size>\n' + '        <segmented>0</segmented>\n' + '        <object>\n                ' +\
            '<name>' + str(labelnum) + '</name>\n                ' + '<pose>Unspecified</pose>\n                ' + \
            '<truncated>0</truncated>\n                ' + '<difficult>0</difficult>\n                ' +\
            '<bndbox>\n                        ' +\
            '<xmin>' + str(1) + '</xmin>\n                        ' +\
            '<ymin>' + str(1) + '</ymin>\n                        ' +\
            '<xmax>' + str(img.shape[1] - 1) + '</xmax>\n                        ' +\
            '<ymax>' + str(img.shape[0] - 1) + '</ymax>\n                ' +\
            '</bndbox>\n        ' +\
            '</object>\n' +\
            '</annotation>'

        f.write(data)
        f.close()
