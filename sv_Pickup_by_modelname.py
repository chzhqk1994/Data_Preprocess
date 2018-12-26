import os
from distutils import dir_util

# 연식에 모델명, 메이커 이름이 붙어있는 데이터 셋 ex) Audi_Audi A7_2015
dataset_path = '/home/hyunwoo/Desktop/Untitled/temp'

# 뽑아낸 모델을 Copy 할 경로
output_path = '/home/hyunwoo/Desktop/Untitled/pickup_output/'


def pickup_model(model):
    for root, dirs, _ in os.walk(dataset_path):
        for i in range(len(model)):
            if model[i].lower() in os.path.basename(root).lower():
                print(os.path.basename(root))
                dir_util.copy_tree(root, output_path + os.path.basename(root))


if __name__ == '__main__':
    # 뽑아낼 차량 메이커 이름을 리스트에 추가
    pickup_model(
        ['AUDI',
         'BMW',
         'BENZ',
         'BENTLEY',
         'CHRYS',
         'CADILLAC',
         'CHEVY',
         'CHRYSLER',
         'CITROEN',
         'DODGE',
         'FERRARI',
         'FIAT',
         'FORD',
         'GMC',
         'HONDA',
         'HYUNDAI',
         'INFINITI',
         'JAGUAR',
         'JEEP',
         'KIA',
         'LAMORGHINI',
         'LAND-ROVER',
         'LEXUS',
         'LINCOLN',
         'MASERATI',
         'MAYBACH',
         'MINI',
         'MUSTANG',
         'NISSAN',
         'OPEL',
         'PEUGEOT',
         'PORSCHE',
         'RENAULT',
         'ROLLS-ROYCE',
         'SAAB',
         'SMART',
         'TOYOTA',
         'VOLKSWAGEN',
         'VOLVO'])
