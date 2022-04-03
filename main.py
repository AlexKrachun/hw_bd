import pickle


class Student:
    def __init__(self, name, lname, father, marks):
        self.name = name
        self.lname = lname
        self.father = father
        self.marks = list(map(int, marks.split()))
        self.sred_ball = round(sum(self.marks) / len(self.marks), 2)

    def __str__(self):
        marksstr = ''
        for i in self.marks:
            marksstr += str(i) + ' '
        return f'{self.name} {self.lname} {self.father} {marksstr} {self.sred_ball}'


with open('input.txt', encoding='utf-8') as f:
    st = [Student(*i.split(' ', 3)) for i in f]

with open('bd.dat', 'wb') as f:
    pickle.dump(st, f)

with open('bd.dat', 'rb') as f:
    students = pickle.load(f)

while True:
    print('com_red <param> - корректировка БД, параметр - номер студента\n'
          'com_sort - сортировка по убыванию среднего балла\n'
          'com_new - создание новой записи в БД\n'
          'com_two - список студентов имеющих двойки\n'
          'com_exit - завершение работы программы\n')
    for i in range(len(students)):
        print(i + 1, students[i])
    print()
    command = input('Введите команду: ')
    if command == 'com_exit':
        exit()

    elif command == 'com_new':
        new_st = Student(*input('Введите через пробел Имя Фамилию Отчество все оценки в одну строку: ').split(' ', 3))
        students.append(new_st)
        with open('bd.dat', 'wb') as f:
            pickle.dump(students, f)

    elif command == 'com_sort':
        print(*sorted(students, key=lambda x: x.sred_ball, reverse=True), sep='\n')

    elif command == 'com_two':
        for stud in students:
            if 2 in stud.marks:
                print(stud)

    elif 'com_red' in command:
        param = int(command.split()[1]) - 1
        students[param] = input(str(students[param]) + ': ')
        with open('bd.dat', 'wb') as f:
            pickle.dump(students, f)

    with open('bd.dat', 'rb') as f:
        students = pickle.load(f)
    print('\n###########################\n')


