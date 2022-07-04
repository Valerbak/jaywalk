# создаю нужные штуки
frame = {}
person = {}
ppp = list()
counter_of_persons_in_frame = list()
frame_dict = {}
frame_list = list()
count = 0
# открываю файл, он записывается в file как строка
with open(r"D:\Desktop\practice\results_road_2\test_track_res.txt", 'rt') as file:
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
        if frame_value != ['']:
            for value in frame_value:
                # удаляю пробелы в начале и конце строки иделю строку по пробелам
                fv = value.strip().split()
                # первый элемент в строке - ключ (номер человека)
                key2 = int(fv[0])
                # привожу остальное содержимое к FLOAT
                ww = ([float(i) for i in fv[1:]])
                # создаю словарь со значениями для людей
                person[key2] = ww
                # создаю список со словарями с людьми
                asd = person.copy()
                ppp.append(asd)
                person.clear()
            # считаю сколько всего людей в каждом кадре
            counter_of_persons_in_frame.append(len(frame_value))
        else:
            counter_of_persons_in_frame.append(0)

    # создаю список с кадрами
    for i in counter_of_persons_in_frame:
        frame_list.append(ppp[count:count + i])
        count += i
    # заполняю словарь кадров
    for o in range(len(frame_list)):
        frame_dict[o] = frame_list[o]

# функция для подсчета тангенса прямой по 2ум точкам
def tang(x_down, y_down, x_up, y_up):
    tan = (y_down - y_up) / (x_down - x_up)
    if tan > 0:
        return 1
    else:
        return 0


dict_if_smb = dict()
# координаты дороги
# 1- левый край, 2- второй
x1_down = 0
y1_down = 555
x1_up = 1754
y1_up = 240
x2_down = 1040
y2_down = 1080
x2_up = 1871
y2_up = 301

# вычисление тангенса наклона левого и правого края дороги
tan_left_line = tang(x1_down, y1_down, x1_up, y1_up)
tan_right_line = tang(x2_down, y2_down, x2_up, y2_up)

# в зависимости от тангенса меняется знак при проверке
def chek_if_on_road(tan1, tan2, x1_down, y1_down, x1_up, y1_up, x2_down, y2_down, x2_up, y2_up, x_middle, y_middle):
    if (tan1 == 0) and (tan2 == 0):
        if_person_on_road = (
                (((x_middle - x1_down) / (x1_up - x1_down)) - ((y_middle - y1_down) / (y1_up - y1_down))) > 0 and
                (((x_middle - x2_down) / (x2_up - x2_down)) - ((y_middle - y2_down) / (y2_up - y2_down))) < 0)
    elif (tan1 == 1) and (tan2 == 1):
        if_person_on_road = (
                (((x_middle - x1_down) / (x1_up - x1_down)) - ((y_middle - y1_down) / (y1_up - y1_down))) < 0 and
                (((x_middle - x2_down) / (x2_up - x2_down)) - ((y_middle - y2_down) / (y2_up - y2_down))) > 0)
    elif (tan1 == 1) and (tan2 == 0):
        if_person_on_road = (
                (((x_middle - x1_down) / (x1_up - x1_down)) - ((y_middle - y1_down) / (y1_up - y1_down))) < 0 and
                (((x_middle - x2_down) / (x2_up - x2_down)) - ((y_middle - y2_down) / (y2_up - y2_down))) < 0)
    elif (tan1 == 0) and (tan2 == 1):
        if_person_on_road = (
                (((x_middle - x1_down) / (x1_up - x1_down)) - ((y_middle - y1_down) / (y1_up - y1_down))) > 0 and
                (((x_middle - x2_down) / (x2_up - x2_down)) - ((y_middle - y2_down) / (y2_up - y2_down))) > 0)
    return if_person_on_road


number_of_frame = 0
for dict_frame_value in frame_dict.values():
    jaywalk = 0
    if dict_frame_value:
        for every_person in dict_frame_value:
            for dict_pers_value in every_person.values():
                # вычисление серидины рамки
                x_middle = (dict_pers_value[0] + dict_pers_value[2]) / 2
                y_middle = (dict_pers_value[1] + dict_pers_value[3]) / 2
                # проверка на дороге ли человек
                if chek_if_on_road(tan_left_line, tan_right_line, x1_down, y1_down, x1_up, y1_up, x2_down, y2_down,
                                   x2_up, y2_up, x_middle, y_middle):
                    jaywalk = 1
                    # print(jaywalk)
                if jaywalk == 1:
                    break
    dict_if_smb[number_of_frame] = jaywalk
    number_of_frame += 1

# запись значений в файл
with open(r"D:\Desktop\practice\results_road_2\results2.txt", 'w') as res_file:
    for key in dict_if_smb:
        s = str(key)
        s += ':' + ' '
        s += str(dict_if_smb.get(key))
        s += '\n'
        res_file.write(s)
