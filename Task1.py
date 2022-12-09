# 1 Напишите программу, удаляющую из файла все слова, содержащие "абв".

with open('file_from_task1.txt', 'rb+') as f:
    s = ' '.join(list(filter(lambda x: not 'абв' in x, f.read().decode('utf-8').split())))
    f.seek(0)
    f.write(s.encode())
    f.truncate()