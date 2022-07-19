#берем из файла список идентивикаторов постов
with open('list_group_id.txt') as file:
    l = (15755094, 30179569, 91452083, 142918777, 170528132)
    cash = dict()
    k = list()
    for i in range(15):
        s = [file.readline()]
        s = [line.rstrip(',\n') for line in s]
        k.append(int(s[0]))
    print(k)
    cash[15755094] = k[0:3]
    cash[30179569] = k[3:6]
    cash[91452083] = k[6:9]
    cash[142918777] = k[9:12]
    cash[170528132] = k[12:15]
#записываем в файл новый список идентификаторов постов
with open('list_group_id.txt','w') as file:
    k = list()
    for id_g,id_p in cash.items():
        for i in id_p:
            k.append(i)

    for i in k:
        print(i)
        file.write(str(i) +',\n')
    #print(k)
