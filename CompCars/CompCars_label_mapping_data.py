from distutils import dir_util
from scipy.io import loadmat
from shutil import move
import distutils
import os

#   $ find . -maxdepth 3 -type f -delete   >>  현재 디렉토리의 depth 만큼의 하위 디렉토리를 뒤지고 파일들만 전부 삭제

# Load .mat file
matrix = loadmat("./CompCar_label/make_model_name.mat")

dataset_path = '/home/hyunwoo/Desktop/CompCar/dataset/data/image'
output_path = '/home/hyunwoo/Desktop/Untitled/data_output/'

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


def save_list_to_file(make_list, model_list):
    with open('make_labels.txt', 'w') as f:
        for i in range(len(make_list)):
            print(i, make_list[i])
            f.write("%s %s\n" % (i + 1, make_list[i]))

    with open('model_labels.txt', 'w') as f:
        for i in range(len(model_list)):
            print(i, model_list[i])
            if str(model_list[i]) == '':
                model_list[i] = 'unknown'
            f.write("%s %s\n" % (i + 1, model_list[i]))


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
    # topdown 옵션을 False 로 줌으로써 하위 디렉토리먼저 반환
    for root, dirs, _ in os.walk('/home/hyunwoo/Desktop/Untitled/data_output', topdown=False):
        level = root.replace('/home/hyunwoo/Desktop/Untitled/data_output', '').count(os.sep)

        if level == 3:
            model_path = os.path.abspath(os.path.join(root, os.pardir))
            make_path = os.path.abspath(os.path.join(model_path, os.pardir))

            for i in os.listdir(model_path):
                # print('============== 연식 =================')
                # print(i)
                # print('os.listdir(model_path) : ', os.listdir(model_path))
                # print('original : ', model_path + '/' + i)
                # print('modified : ', model_path + '/' + make_names[int(os.path.basename(make_path)) - 1] + '_' + model_names[int(os.path.basename(model_path)) - 1] + '_' + i)
                move(model_path + '/' + i, model_path + '/' + make_names[int(os.path.basename(make_path)) - 1] + '_' + model_names[int(os.path.basename(model_path)) - 1] + '_' + i)

    for root, dirs, _ in os.walk('/home/hyunwoo/Desktop/Untitled/data_output', topdown=False):
        level = root.replace('/home/hyunwoo/Desktop/Untitled/data_output', '').count(os.sep)

        if level == 3:
            model_path = os.path.abspath(os.path.join(root, os.pardir))
            make_path = os.path.abspath(os.path.join(model_path, os.pardir))

            for i in os.listdir(make_path):
                # print('============== 모델명 =================')
                # print('os.listdir(make_path) : ', os.listdir(make_path))
                # print(i)
                # print(make_path + '/' + i)
                # print(make_path + '/' + model_names[int(i) - 1])
                move(make_path + '/' + i, make_path + '/' + model_names[int(i) - 1])

    for root, dirs, files in os.walk('/home/hyunwoo/Desktop/Untitled/data_output'):
        level = root.replace('/home/hyunwoo/Desktop/Untitled/data_output', '').count(os.sep)

        if level == 1:
            move(output_path + os.path.basename(root), output_path + make_names[int(os.path.basename(root)) - 1])


# 특정 디렉토리와 하위 파일들을 다른 디렉토리로 복사, 원본의 파일들은 그대로 있음
def copy_bottom_dir_to_top():
    copy_to_path = '/home/hyunwoo/Desktop/Untitled/temp'
    for root, dirs, _ in os.walk(output_path):
        level = root.replace(output_path, '').count(os.sep)

        if level == 1:
            print(dirs)
            print(root)
            print(output_path)
            distutils.dir_util.copy_tree(root + '/', copy_to_path)


if __name__ == '__main__':
    make_list('make_names', 'model_names')  # model_names : 163, make_names : 1711
    save_list_to_file(make_names, model_names)
    # print_dir_hierarchy()
    # copy_file_dir_hierarchy()
    # modify_dir_name()
    # copy_bottom_dir_to_top()
