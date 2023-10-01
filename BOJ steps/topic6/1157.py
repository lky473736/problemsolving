'''# 대소문자 변경 : https://blockdmask.tistory.com/416

sinput = input()
lower_sinput = sinput.lower()

charlist = []
charnum_list = []

for i in range(len(lower_sinput)):
    charlist.append(lower_sinput[i])

charset = set(charlist)

for j in charset:
    if charlist.count(j) not in charnum_list:
        charnum_list.append(charlist.count(j))

max_count = max(charnum_list)

if charnum_list.count(max_count) > 1:
    print('?')
else:
    max_char = list(charset)[charnum_list.index(max_count)].upper()
    print(max_char)'''

sinput = input()
lower_sinput = sinput.lower()

charlist = []
charnum_list = []

for i in range(len(lower_sinput)):
    charlist.append(lower_sinput[i])

charset = set(charlist)

max_count = 0
max_char = ''

for j in charset:
    char_count = charlist.count(j)
    if char_count > max_count:
        max_count = char_count
        max_char = j
    elif char_count == max_count:
        max_char = '?'

print(max_char.upper())
