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
f = open('alfabeto.txt', 'w')
for i in alfabeto:
    lettera = i
    lettera = lettera.upper()
    print('            \'', lettera, '\'', ': ', j, ',')
    j = j+1