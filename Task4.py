# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

# aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
# 4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff

with open('first_file_from_task4.txt', 'r') as f:
    s = f.read().split('\n')

def main(s):
    st = ''
    for i in s:
        if not str(i).isalpha():
            st += decode(i) + '\n'
        else:
            st += compression(i) + '\n'
    return st
    
def decode(st):
    n = ''
    strin = ''
    for i in st:
        if str(i).isdigit():
            n += i
        else:
            strin += str(i) * int(n)
            n = ''
    return strin   

def compression(st):
    index = 1
    first = st[0]
    count = 1
    second = ''
    while index < len(st):
        if first == st[index]:
            count += 1
            index += 1
        else:
            second += str(count) + st[index - 1]
            first = st[index]
            count = 1
            index += 1
    second += str(count) + st[index - 1]
    return second 

with open('second_file_from_task4.txt', 'w') as w:
    w.write(main(s))
