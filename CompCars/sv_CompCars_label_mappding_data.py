from distutils import dir_util
from scipy.io import loadmat
from shutil import move
import distutils
import os

#   $ find . -maxdepth 3 -type f -delete   >>  현재 디렉토리의 depth 만큼의 하위 디렉토리를 뒤지고 파일들만 전부 삭제

# sv_data > 제조사로 나뉘어 있지 않고 모델별로마 나뉘어져 있음

# Load .mat file
matrix = loadmat("./CompCar_label/sv_make_model_name.mat")

dataset_path = '/home/hyunwoo/Desktop/CompCar/dataset/sv_data/image'
output_path = '/home/hyunwoo/Desktop/Untitled/sv_output/'

make_names = []
model_names = []


def make_dir(label_type):
    tmp = []
    cnt = 0
    for idx in range(len(matrix[label_type])):
        tmp.append(str(matrix[label_type][idx][0]))
        make_names.append(tmp[idx][2:-2])

        if len(str(matrix[label_type][idx][0])) == 2:  # 값이 비어있는 곳은 pass, 아닌곳은 디렉토리 생성(index 맞추기 위함)
            print(str(matrix[label_type][idx][0]))
            cnt += 1
            pass

        else:
            # 이름 : 숫자
            # if not os.path.exists(output_path + str(idx + 1)):
            #     os.makedirs(output_path + str(idx + 1))

            # 이름 : 모델명
            # if not os.path.exists(output_path + make_names[idx]):
            #     os.makedirs(output_path + make_names[idx])

            # 이름 : 숫자 + 모델명
            if not os.path.exists(output_path + str(idx) + make_names[idx]):
                os.makedirs(output_path + str(idx) + make_names[idx])


def make_list(label_type):
    cnt = 0

    # make_names 리스트 생성
    tmp = []
    for idx in range(len(matrix[label_type])):
        if len(str(matrix[label_type][idx][0])) == 2:  # 값이 비어있는 곳은 공백으로 둠(index 맞추기 위함)
            tmp.append(str(matrix[label_type][idx][0]))
            make_names.append(tmp[idx][0])
            cnt += 1

        else:
            tmp.append(str(matrix[label_type][idx][0]))
            make_names.append(tmp[idx][2:-2])

    # model_names 리스트 생성
    tmp = []
    for idx in range(len(matrix[label_type])):
        if len(str(matrix[label_type][idx][1])) == 2:  # 값이 비어있는 곳은 공백으로 둠(index 맞추기 위함)
            tmp.append(str(matrix[label_type][idx][1]))
            model_names.append('')
            cnt += 1

        else:
            tmp.append(str(matrix[label_type][idx][1]))
            model_names.append(tmp[idx][2:-2])

    print("make_names : ", make_names)
    print("len of make_names : ", len(make_names))
    print("")
    print("model_names : ", model_names)
    print("len of model_names : ", len(model_names))
    print("")

    return make_names, model_names


def copy_file_dir_hierarchy():
    # 디렉토리를 통째로 복사, 이름이 겹치면 overwrite
    distutils.dir_util.copy_tree(dataset_path, output_path)


def print_dir_hierarchy():
    for root, dirs, files in os.walk(dataset_path):
        level = root.replace(dataset_path, '').count(os.sep)

        # 계층 레벨이 1 이면 make_names 를 참조
        if level == 1:
            print(make_names[int(os.path.basename(root)) - 1])

        # 계층 레벨이 2 이면 model_names 를 참조
        if level == 2:
            print("    ", model_names[int(os.path.basename(root)) - 1])


def modify_dir_name():
    # root 는 상위폴더 이름
    # dirs 는 root 폴더의 (상위폴더의) 하위폴더 이름들을 list 로 받음
    for root, dirs, files in os.walk(dataset_path):
        level = root.replace(dataset_path, '').count(os.sep)

        # depth 가 1 일 때
        if level == 1:
            print(os.path.basename(root))

            # 이름 변경
            move(output_path + os.path.basename(root), output_path + model_names[int(os.path.basename(root)) - 1])


if __name__ == '__main__':
    make_list('sv_make_model_name')  # model_names : 163, make_names : 1711
    # print_dir_hierarchy()
    # copy_file_dir_hierarchy()
    modify_dir_name()
