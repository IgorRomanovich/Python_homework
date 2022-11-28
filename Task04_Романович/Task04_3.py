# Вывести из двух файлов слова, которые есть в обоих файлах.

def in2file():
    rs1 = ''
    rs2 = ''
    rs = []
    for ln in f1:
        rs1 += ln.casefold()
    for ln in f2:
        rs2 += ln.casefold()
    ln1 = rs1.split()
    l2 = rs2.split()
    for word1 in ln1:
        for word2 in l2:
            if word1 == word2:
                rs.append(word1)
    return set(rs)


f1 = open('in.txt', '+r')
f2 = open('in.txt', '+r')
print(in2file())
