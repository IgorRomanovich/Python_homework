# Найти в файле самое частовстречаемое слово.


def freq():
    resline = ''
    resword = ''
    b = 0
    for i in f:
        resline += i.casefold()
    lnarray = resline.split()
    ln = len(lnarray)
    for i in range(ln):
        count = 0
        n = ln
        j = i + 1
        while j < n:
            if lnarray[i] != lnarray[j]:
                j += 1
            else:
                count += 1
                lnarray.pop(j)
                n -= 1
        if count > b:
            b = count
            resword = lnarray[i]
        elif count == b:
            resword += ', ' + lnarray[i]
    if b == 0:
        print('All words occur once!')
    elif count == b:
        print('Words that occur the maximum number of times: ', resword)
    else:
        print('The most frequently occurring word is: ', resword)


f = open('in.txt', '+r')
freq()
