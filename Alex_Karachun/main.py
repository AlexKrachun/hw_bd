import pickle


class Tour:
    def __init__(self, number: str, leave: str, arrive: str)-> None:
        self.number: int = int(number)
        self.leave: str = leave
        self.arrive: str = arrive

    def __str__(self)-> str:
        return f'{str(self.number)} {self.leave} --> {self.arrive}'


file_name = input("Введите имя файла: ")
with open('last_bd.txt') as f:
    if file_name not in f.readline():
        with open('first_data.txt', encoding='utf-8') as f:
            a = [Tour(*i.replace('\n', '').split('\\')) for i in f]

        with open(f'{file_name}.dat', 'wb') as f:
            pickle.dump(a, f)
    with open('last_bd.txt', 'a') as f1:
        print(file_name, end=' ', file=f1)


with open(f'{file_name}.dat', 'rb') as f:
    t_list = pickle.load(f)


while True:
    print('\nСписок команд:\n'
          'com_edit_<param> - корректировать запись, номер которой указан в <param>\n'
          'com_new - создать новую запись\n'
          'com_sort - сортировать по убыванию номера маршрута\n'
          'com_leave_<param> - покозать маршруты начинающиеся из пункта указанного в <param>\n'
          'com_arrive_<param> - покозать маршруты заканчивающиеся в пункте указанном в <param>\n'
          'com_exit - завершить выполнение программы\n')
    print(*t_list, sep='\n')
    com = input('Введите команду: ')
    if com == 'com_exit':
        exit()
    elif 'com_edit' in com:
        param = int(com.split('_')[-1])
        ind = -1
        for i in range(len(t_list)):
            if t_list[i].number == param:
                ind = i
                break
        print(t_list[ind])
        t_list[ind] = Tour(*input('Введите данные в формате <номер>\<от куда маршрут>\<куда маршрут>: ').split('\\'))
        with open(f'{file_name}.dat', 'wb') as f:
            pickle.dump(t_list, f)
        print('Поправки были внесены в БД')
    elif com == 'com_new':
        t_list.append(Tour(*input('Введите данные в формате <номер>\<от куда маршрут>\<куда маршрут>: ').split('\\')))
        with open(f'{file_name}.dat', 'wb') as f:
            pickle.dump(t_list, f)
        print('Данные были внесены в БД')
    elif com == 'com_sort':
        print('======================')
        print(*sorted(t_list, key=lambda t: t.number), sep='\n')
        print('======================')
    elif 'com_leave_' in com:
        param = com.split('_')[-1]
        cou = 0
        print('======================')
        for t in t_list:
            if t.leave == param:
                print(t)
                cou += 1
        if cou == 0:
            print('Таки маршруов нет')
        print('======================')
    elif 'com_arrive_' in com:
        param = com.split('_')[-1]
        cou = 0
        print('======================')
        for t in t_list:
            if t.arrive == param:
                print(t)
                cou += 1
        if cou == 0:
            print('Таки маршруов нет')
        print('======================')



