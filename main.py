# создаю нужные штуки
frame = {}
person = {}
ppp = list()
counter_of_persons_in_frame = list()
frame_dict = {}
frame_list = list()
count = 0
# открываю файл, он записывается в file как строка
with open(r"D:\Desktop\practice\results_demo8\test_track_res.txt", 'rt') as file:
    # построчно разбираю текст из файла
    for line in file:
        # убираю из строки знаки переноса на следующую строку и пробелы в начале и конце строки
        line = line.strip()
        # если строка не пустая тогда работаем с ней дальше
        if line != '':
            # разделяю содержимое на ключ и значение в словаре
            # ключ - номер кадра
            key1 = int(line[0:6])
            w = line[8:-1].strip().split(';')
            frame[key1] = w
            # работаю со значениями в словаре
    for frame_value in frame.values():
        # резделяю строку по ; и удаляю пробелы в начале и конце строки
        # работаю дальше в разделенных строчках
        for value in frame_value:
            # удаляю пробелы в начале и конце строки иделю строку по пробелам
            fv = value.strip().split()
            # первый элемент в строке - ключ (номер человека)
            key2 = int(fv[0])
            # привожу остальное содержимое к FLOAT
            ww = ([float(i) for i in fv[1:]])
            # создаю словарь со значениями для людей
            person[key2] = ww
            # забыда что я тут сделала
            # ну по сути создаю список со словарями с людьми
            asd = person.copy()
            ppp.append(asd)
            person.clear()
        # считаю сколько всего людей в каждом кадре
        counter_of_persons_in_frame.append(len(frame_value))
        # print(counter_of_persons_in_frame)
    # создаю список с кадрами
    for i in counter_of_persons_in_frame:
        frame_list.append(ppp[count:count + i])
        count += i
    # заполняю словарь кадров
    for o in range(len(frame_list)):
        frame_dict[o] = frame_list[o]


dict_if_smb = dict()
# координаты дороги
x1_down = 815
y1_down = 1080
x1_up = 726
y1_up = 0
a_x1 = x1_up - x1_down
a_y1 = y1_up - y1_down
x2_down = 1659
y2_down = 1080
x2_up = 1160
y2_up = 0
a_x2 = x2_up - x2_down
a_y2 = y2_up - y2_down
number_of_frame = 0
for dict_frame_value in frame_dict.values():
    jaywalk = 0
    for every_person in dict_frame_value:
        for dict_pers_value in every_person.values():
            # print(dict_pers_value)
            x_middle = (dict_pers_value[0] + dict_pers_value[2]) // 2
            y_middle = (dict_pers_value[1] + dict_pers_value[3]) // 2
            # print(x_middle, y_middle)
            if ((((x_middle - x1_down) / a_x1) - (y_middle - y1_down) / a_y1) < 0 and
                    (((x_middle - x2_down) / a_x2) - (y_middle - y2_down) / a_y2) > 0):
                jaywalk = 1
                # print(jaywalk)
            if jaywalk==1:
                break
    dict_if_smb[number_of_frame] = jaywalk
    number_of_frame += 1

# запись значений в файл
with open(r"D:\Desktop\practice\results_demo8\results.txt", 'w') as res_file:
    for key in dict_if_smb:
        s = str(key)
        s += ':' + ' '
        s += str(dict_if_smb.get(key))
        s += '\n'
        res_file.write(s)

