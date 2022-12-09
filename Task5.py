# Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.

# *Пример:* 

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
import copy


def main():
    lst = [1, 5, 2, 3, 4, 6, 1, 7]
    mass = list()
    for j in range(len(lst) - 1):
        for i in range(len(lst) - 1):
            sequence(two_number(lst, j, i), mass)
    return mass

def sequence(lst, mass, *index):
    values = list()
    step = 1
    flag_first = True
    while flag_first:
        index_first = 0
        index_second = index_first
        flag_second = True
        count = 0
        values.append(lst[0])
        while flag_second:
            if index == index_second:
                index_second += 1
                continue
            if count < step:
                if lst[index_first] < lst[index_second]:
                    values.append(lst[index_second])
                    index_first = index_second
                    count += 1
                elif index_second < len(lst) - 1:
                    index_second += 1
                else:
                    values.clear()
                    flag_first = False
                    break

            else:
                step += 1
                flag_second = False
        if values != []:
            if not mass.count(values):
                mass.append(copy.copy(values))
            values.clear()
             
    return mass

def two_number(lst, index, index_sec):
    flag = True
    while flag:
        res = list()
        for i in range(len(lst)):
            if i < index or i > index_sec:
                res.append(lst[i])
 
        flag = False
    return res  

m = main()
print(f'Значения нарастающих последовательностей: {m}')



