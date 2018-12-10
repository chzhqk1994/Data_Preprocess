import os
import cv2
import numpy as np
import distutils
from distutils import dir_util
from shutil import copyfile

test_image_dir = './CompCar_label/test_image/'

dataset_path = '/home/hyunwoo/Desktop/Untitled/sv_output/'
# dataset_path = './CompCar_label/test_image/'
output_path = '/home/hyunwoo/Desktop/Untitled/sv_time_output/'

hist_list = []

# threshold = 76.67734425136506  # histogram average
threshold = 60


def copy_dir():
    # Copy dataset
    # 디렉토리를 통째로 복사, 이름이 겹치면 overwrite
    distutils.dir_util.copy_tree(dataset_path, output_path)


# 데이터셋의 모든 이미지들의 hist 를 저장하고 평균값을 산출
def show_histogram():
    for root, dirs, file in os.walk(dataset_path):
        for i in range(len(file)):
            file_dir = root+ '/' + file[i]

            image = cv2.imread(file_dir, cv2.IMREAD_GRAYSCALE)

            # channels : grayscale 인 경우 [0]
            # hist = cv2.calcHist(image, channels=[0], mask=None, histSize=[256], ranges=[0, 256])

            # hist, bins = np.histogram(image.ravel(), 256, [0, 256])

            average = image.mean(axis=0).mean(axis=0)
            print(average)

            if average > threshold:
                print('Day')
            else:
                print('Night')

            print('============')

            cv2.imshow('image', image)
            cv2.waitKey(0)


# 데이터셋의 모든 이미지의 histogram 값을 리스트에 저장하고 평균 값 출력
def calculate_hist_mean():

    for root, dirs, file in os.walk(dataset_path):
        for i in range(len(file)):
            path = root + '/' + file[i]
            print(path)

            image = cv2.imread(path)
            average = image.mean()
            hist_list.append(average)
            # print(hist_tem[i])
        print('============')

    # print(np.mean(hist_list))
    print(np.mean(hist_list))


def separate_time():
    for root, dirs, file in os.walk(dataset_path):
        # for i in range(len(file)):
        print('root : ', len(file))
        print('file length : ', len(file))
        print('file length : ', len(file))
        print('os.path.basename(root) : ', os.path.basename(root))
        for i in range(len(file)):
            path = root + '/' + file[i]

            image = cv2.imread(path)
            average = image.mean()

            if average > threshold:
                print(root + '/day/' + file[i])
                if not os.path.exists(output_path + str(os.path.basename(root)) + '/' + '/day/'):
                    os.makedirs(output_path + str(os.path.basename(root)) + '/' + '/day/')
                copyfile(dataset_path + str(os.path.basename(root)) + '/' + file[i], output_path + str(os.path.basename(root)) + '/day/' + file[i])

            else:
                print(root + '/night/' + file[i])
                if not os.path.exists(output_path + str(os.path.basename(root))+ '/' + '/night/'):
                    os.makedirs(output_path + str(os.path.basename(root))+ '/' + '/night/')
                copyfile(dataset_path + str(os.path.basename(root))+ '/' + file[i], output_path + str(os.path.basename(root)) + '/night/' + file[i])


if __name__ == '__main__':
    # copy_dir()
    # show_histogram()
    # calculate_hist_mean()
    separate_time()