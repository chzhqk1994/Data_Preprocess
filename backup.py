from scipy.io import loadmat
import distutils
from distutils import dir_util
import os

# Load .mat file
matrix = loadmat("./CompCar_label/make_model_name.mat")

dataset_path = 'C:/Users/qisens-n_hyunwoo/Desktop/image'
output_path = 'C:/Users/qisens-n_hyunwoo/Desktop/project/Data_Preprocess/CompCar_label/CompCar_result/'

make_names = []
model_names = []


# def make_dir(label_type):
#     cnt = 0
#     for idx in range(len(matrix[label_type])):
#         tmp.append(str(matrix[label_type][idx][0]))
#         make_names.append(tmp[idx][2:-2])
#
#         if len(str(matrix[label_type][idx][0])) == 2:  # 값이 비어있는 곳은 pass, 아닌곳은 디렉토리 생성(index 맞추기 위함)
#             print(str(matrix[label_type][idx][0]))
#             cnt += 1
#             pass
#
#         else:
#             # 이름 : 숫자
#             # if not os.path.exists(output_path + str(idx + 1)):
#             #     os.makedirs(output_path + str(idx + 1))
#
#             # 이름 : 모델명
#             # if not os.path.exists(output_path + make_names[idx]):
#             #     os.makedirs(output_path + make_names[idx])
#
#             # 이름 : 숫자 + 모델명
#             if not os.path.exists(output_path + str(idx) + make_names[idx]):
#                 os.makedirs(output_path + str(idx) + make_names[idx])
#


def make_list(label_type, lable_type2):
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
    for idx in range(len(matrix[lable_type2])):
        if len(str(matrix[lable_type2][idx][0])) == 2:  # 값이 비어있는 곳은 공백으로 둠(index 맞추기 위함)
            tmp.append(str(matrix[lable_type2][idx][0]))
            model_names.append('')
            cnt += 1

        else:
            tmp.append(str(matrix[lable_type2][idx][0]))
            model_names.append(tmp[idx][2:-2])

    print("make_names : ", make_names)
    print("len of make_names : ", len(make_names))
    print("")
    print("model_names : ", model_names)
    print("len of model_names : ", len(model_names))
    print("")


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
    for root, dirs, files in os.walk(output_path):
        # print(root.replace(output_path, ''))
        print(os.path.basename(root))
        level = root.replace(output_path, '').count(os.sep)

        # 계층 레벨이 1 이면 make_names 를 참조
        if level == 0:
            print(os.path.basename(root) + ' : level 1')
            # os.rename(output_path + os.path.basename(root), output_path + make_names[int(os.path.basename(root))-1])
            # print(make_names[int(os.path.basename(root)) - 1])

        # 계층 레벨이 2 이면 model_names 를 참조
        # if level == 1:
        #     print(os.path.basename(root) + ' : level 2')
        #     os.rename(output_path + os.path.basename(root), output_path + model_names[int(os.path.basename(root))-1])
        #     # print("    ", model_names[int(os.path.basename(root)) - 1])


if __name__ == '__main__':
    make_list('make_names', 'model_names')  # model_names : 163, make_names : 1711
    copy_file_dir_hierarchy()
    modify_dir_name()
