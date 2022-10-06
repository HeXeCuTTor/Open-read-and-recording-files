file_1 =  open('1.txt', 'rt',encoding = 'utf8')
res_1 = file_1.readlines()
times_1 = len(res_1)
res_1 = ' '.join(res_1)
name_1 = '1.txt'

file_2 =  open('2.txt', 'rt',encoding = 'utf8')
res_2 = file_2.readlines()
times_2 = len(res_2)
res_2 = ' '.join(res_2)
name_2 = '2.txt'

file_3 =  open('3.txt', 'rt',encoding = 'utf8')
res_3 = file_3.readlines()
times_3 = len(res_3)
res_3 = ' '.join(res_3)
name_3 = '3.txt'

if times_1 < times_2 and times_1 < times_3:
    print(f'{name_1}\n{times_1}\n{res_1}\n')
    if times_2 < times_3:
        print(f'{name_2}\n{times_2}\n{res_2}\n{name_3}\n{times_3}\n{res_3}')
    else:
        print(f'{name_3}\n{times_3}\n{res_3}\n{name_2}\n{times_2}\n{res_2}')
elif times_1 > times_2 and times_1 < times_3 or times_1 < times_2 and times_1 > times_3:
    if times_2 < times_3:
        print(f'{name_2}\n{times_2}\n{res_2}\n{name_1}\n{times_1}\n{res_1}\n{name_3}\n{times_3}\n{res_3}')
    else:
        print(f'{name_3}\n{times_3}\n{res_3}\n{name_1}\n{times_1}\n{res_1}\n{name_2}\n{times_2}\n{res_2}')
else:
    if times_2 < times_3:
        print(f'{name_2}\n{times_2}\n{res_2}\n{name_3}\n{times_3}\n{res_3}')
    else:
        print(f'{name_3}\n{times_3}\n{res_3}\n{name_2}\n{times_2}\n{res_2}')
    print(f'{name_1}\n{times_1}\n{res_1}\n')