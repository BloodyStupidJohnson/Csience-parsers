import zlib
import base64


# Деархиватор

# file = open("/home/rincewind/Рабочий стол/Science shit/700.tab","r")
# i=0
# for s in file:
#     s = s.strip().split("\t")
#     e = open("/home/rincewind/Рабочий стол/Science shit/DIO/"+str(i)+".txt", "w")
#     e.write(s[0] + "\n")
#     e.write((zlib.decompress(base64.standard_b64decode(s[len(s)-1]),wbits = zlib.MAX_WBITS | 16)).decode("UTF-8"))
#     print(i," файлов обработано")
#     e.close()
#     i+=1
# file.close()

# Фильтр
def wordfix_1(s):
    if (s == '') or (s == " "):
        return None
    zp = ['!', '?', '/', '/', '\\', ',', '.', '<', '>', '{', '}', '[', ']', '*', '^', ';', ':', '-']
    i = 0
    while i < len(s):
        if s[i] in zp:
            s = s[:i] + s[i + 1:]
        elif s[i] == '\n':
            s = s[:i] + ' ' + s[i + 1:]
        i += 1
    ls = []
    s = s.split(" ")
    for i in range(0, len(s)):
        ls.append(len(s[i]))
    mc = 0
    nm = []
    while True:
        floor = len(ls)
        if (mc == floor) or (len(ls) == 0):
            break
        if ls[mc] == 1:
            row = mc
            x = mc
            while True:
                if ls[x] == 1:
                    row += 1
                x += 1
                if x >= len(ls):
                    break
                if row < x:
                    break
            nword = s[mc:row]
            nm.append(''.join(nword))
            mc = row
        else:
            nm.append(s[mc])
            mc += 1
    return ' '.join(nm)

#Фильтратор
# for i in range(0,9999):
#     s = ''
#     f = open("/home/rincewind/Рабочий стол/Science shit/DIO/"+str(i)+".txt", 'r')
#     for line in f:
#         s = s + line
#     f = open("/home/rincewind/Рабочий стол/Science shit/DIO/"+str(i)+".txt", 'w')
#     if wordfix_1(s)!=None:
#         f.write(wordfix_1(s))
#     f.close()
#     print("Файл № ",i," готов.")