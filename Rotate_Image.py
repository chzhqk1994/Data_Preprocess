import os
from PIL import Image
import glob

file_dir = '/Users/song/Desktop/test_img001/good/'
save_dir = '/Users/song/Desktop/test_img001/good/result/'

angle = 4

# image_file_name = []
valid_images = [".jpg", ".JPG"]  # 골라낼 확장자 지정
for f in os.listdir(file_dir):
    extension = os.path.splitext(f)[1]  # extension : 확장자   >>  splitext 를 이용하여 확장자와 파일이름을 분리하고 확장자만 선택
    if extension.lower() not in valid_images:
        continue
    # image_file_name.append(os.path.split(file_dir + f)[-1])  # 파일 경로에서 경로와 파일 이름을 나누고 이름만 선택
    save_image = Image.open(file_dir + f)
    save_image = save_image.rotate(angle)
    save_image.save(save_dir + f)