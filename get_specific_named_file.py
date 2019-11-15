import os
import cv2
import numpy as np
from collections import Counter

image_path = '/home/qisens/Desktop/test_dataset_2514'
count_th = 2
save_path = '/home/qisens/Desktop/saved_dataset'


# 데이터셋의 모든 이미지의 histogram 값을 리스트에 저장하고 평균 값 출력
def calculate_hist_mean(dataset_path):
    hist_list = []
    for root, dirs, file in os.walk(dataset_path):
        for i in range(len(file)):
            path = root + '/' + file[i]
            print(path)

            image = cv2.imread(path)
            average = image.mean()
            hist_list.append(average)
            # print(hist_tem[i])
        print('============')

    print(np.mean(hist_list))
    return np.mean(hist_list)


# 모든 파일의 접두사 (label) 를 중복하여 리스트에 저장
total_list = []
for (path, dir, files) in os.walk(image_path):
    for file in files:
        file_path = os.path.join(path, file)
        maker_name = str(file).split('_')[0]
        total_list.append(maker_name)


# 중복 저장된 list 를 Counter 함수를 이용해 갯수를 세고 dictionary 로 반환
count_dict = Counter(total_list)

# dictionary 의 각 key 의 value 가 count_th 보다 작으면 (이미지 수가 threshold 보다 적으면) dictionary 에서 삭제
for key in [key for key in count_dict if count_dict[key] < count_th]:
    del count_dict[key]

# 이미지 전체의 histogram 평균 계산
history_mean = calculate_hist_mean(image_path)
print(history_mean)

# threshold 보다 큰 value 를 가진 key 에 해당하는 이미지들의 histogram 이 histogram_mean 보다 크면 출력
# >> ex) 100 개 이상의 이미지 파일을 가진 제조사 이미지들 중 밝기가 평균 이상인 이미지만 처리
for (path, dir, files) in os.walk(image_path):
    for file in files:
        if str(file).split('_')[0] in count_dict.keys():
            file_path = path + '/' + file
            image = cv2.imread(file_path)
            average = image.mean()

            if average > history_mean:
                print(file_path)

