import os

# 오리지널 filtered 폴더와 original 폴더를 비교하여 중복되는 것이 있으면 original 에서 삭제
filtered_path = '/home/qisens/Desktop/song/Qt/img001/test/filtered/'
original_path = '/home/qisens/Desktop/song/Qt/img001/test/original/'

filtered_dir = os.listdir(filtered_path)
original_dir = os.listdir(original_path)

filtered_item=[]
original_item=[]

for file in filtered_dir:
    filtered_item.append(file)

for file in original_dir:
    if file[:2] == '._':
        os.remove(original_path+file)
    original_item.append(file)

for i in range(len(filtered_item)):
    for j in range(len(original_item)):
        if filtered_item[i] == original_item[j]:
            os.remove(original_path+original_item[i])

print(filtered_item)
print(original_item)
