alfabeto= ['a',
            'b',
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
            'l',
            'm',
            'n',
            'o',
            'p',
            'q',
            'r',
            's',
            't',
            'u',
            'v',
            'w',
            'x',
            'y',
            'z'
            ]
j = 27
m = 1
f = open('alfabeto.txt', 'w')
i = 0
for i in alfabeto:
    lettera = i
    print(m, ': ', '\'', lettera, '\'', ',')
    m = m + 1
i = 0
for i in alfabeto:
    lettera = i
    lettera = lettera.upper()
    print(j, ': ', '\'', lettera, '\'', ',')
    j = j + 1
