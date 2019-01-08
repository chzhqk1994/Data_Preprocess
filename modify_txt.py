from CompCars_label_mapping_data import make_list

file = "test_part_1"
origin_list = []
output_list = []


def load_txt():
    make_names, model_names = make_list('make_names', 'model_names')

    f = open("/home/hyunwoo/Desktop/CompCar/dataset/data/train_test_split/part/" + file + ".txt", mode='r', encoding='utf8')
    while True:
        line = f.readline()
        if not line:
            break
        origin_list.append(line)
    #     print(line)
    # print(origin_list)
    f.close()

    for i in range(len(origin_list)):
        make, model, year, filename = origin_list[i].split("/")

        print(make_names[int(make) - 1] + '/' + model_names[int(model) - 1] + '/' + year + '/' + filename)
        output_list.append(make_names[int(make) - 1] + '/' + model_names[int(model) - 1] + '/' + year + '/' + filename)

    print(output_list)


def save_list_to_file():
    with open("./part/" + file + ".txt", 'w') as f:
        for i in range(len(output_list)):
            print(i, output_list[i])
            f.write("%s" % (output_list[i]))


if __name__ == '__main__':
    load_txt()
    save_list_to_file()
