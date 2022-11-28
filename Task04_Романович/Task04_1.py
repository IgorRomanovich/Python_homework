# Напишите функцию для шифрации и дешифрации информации в файле при помощи азбуки Морзе.
# Используйте 1 пробел между буквами одого слова и 3 пробела между отдельными словами.
# Если расшифрованный текст начинается со слова, первая буква этого слова должна быть заглавной.
# Текст будет состоять только из цифр, букв английского алфавита и пробелов.
# Зашифрованный файл будет иметь префикс cod. и дальше имя исходного файла 


morze = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'j': '.---',
         "i": '..', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-',
         'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
         '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
         '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
         }


def encAndDec(st, m, code):
    if code == 'encode':
        res = ''
        a = ' '
        for i in st:
            if i == ' ' and a == ' ':
                res += '   '
            elif i == ' ' and a != ' ':
                res += '  '
            else:
                res += m[i] + ' '
            a = i
    else:
        res = ''
        word = ''
        i = 0
        ln = len(st)
        while i < ln:
            if st[i:i + 3] == '   ':
                res += ' '
                i += 3
                continue
            if st[i] != ' ':
                word += st[i]
            if st[i + 1:i + 2] == ' ' or i == ln - 1:
                for k, value in m.items():
                    if value == word:
                        res += k
                        word = ''
                        break
            i += 1
    return res


f1 = open('in.txt', '+r')
encf = open('cod.in.txt', '+r')
f2 = open('in2.txt', '+r')
decf = open('cod.in2.txt', '+r')
strEncode = ''
strDecode = ''

for strEncode in f1:
    l = strEncode.strip()
    encf.write(encAndDec('Encoding line:', l, morze) + '\n')

for strDecode in decf:
    l = strDecode.strip()
    f2.write(encAndDec('Decoding line:', l, morze))
