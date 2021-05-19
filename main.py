import os

def verificaPrimo(a, b):
    for i in range (2, a):
        if (a % i) == 0:
            raise ValueError('Il termine a non è primo!')
            os.system('exit')
    for j in range (2, b):
        if (b % j) == 0:
            raise ValueError('Il termine b non è primo!')
            os.system('exit')
def calcoloChiavi(stringaValueError):
    chiave = ''
    stringaValueError = stringaValueError
    while chiave != 'pub' and chiave != 'pri':
        chiave = input('Si necessita della chiave pubblica o privata? Immettere:\n* "pub" per la chiave pubblica;\n* "pri" per la chiave privata.\nScelta: ')
        chiave = chiave.lower()
        if chiave == 'pub':
            chiavePubblica(stringaValueError)
        elif chiave == 'pri':
            chiavePrivata(stringaValueError)
        else:
            print('Scelta non valida. Riprova.')
def chiavePrivata(stringaValueError):
    i = 1
    try:
        a = int(input('inserisci a: '))
        b = int(input('inserisci b: '))
        pub = int(input('inserisci pub: '))
    except ValueError:
        print(stringaValueError)
    verificaPrimo(a, b)
    n = a * b
    z = ((a - 1) * (b - 1))
    while ((pub * i) % z) != 1:
        i = i + 1
        if ((pub * i) % z) == 1:
            pri = i
            print('La chiave privata è: (', pri, ', ', n, ').')
def chiavePubblica(stringaValueError):
    i = 1
    try:
        a = int(input('inserisci a: '))
        b = int(input('inserisci b: '))
        pri = int(input('inserisci pri: '))
    except ValueError:
        print(stringaValueError)
    verificaPrimo(a, b)
    n = a * b
    z = ((a - 1) * (b - 1))
    while ((pri * i) % z) != 1:
        i = i + 1
        if ((pri * i) % z) == 1:
            pub = i
            print('La chiave pubblica è: ', '(', pub, ', ', n, ').')
def crittografaMessaggio(cifrario, stringaValueError, cifrarioFlipped):
    stringaValueError = stringaValueError
    disponibilitaChiavi = ''
    while disponibilitaChiavi != 's' and disponibilitaChiavi != 'n':
        disponibilitaChiavi = input('Si dispone delle chiavi di cifratura?\nScelta (s/n): ')
        disponibilitaChiavi = disponibilitaChiavi.lower()
    if disponibilitaChiavi == 'n':
        chiavePubblica(stringaValueError)
    if disponibilitaChiavi == 's':
        try:
            pub = int(input('Inserire valore di pub: '))
            n = int(input('Inserire valore di n: '))
        except ValueError:
            print(stringaValueError)
            os.system('exit')
    ripetere = ''
    while ripetere != 'stop':
        messaggio = input('Inserisci il valore da cifrare: ')
        # elevamento a potenza: x ** y
        messaggioCifrato = cifrario[messaggio]
        messaggioCifrato = (messaggioCifrato ** pub) % n
        messaggioCifratoStringa = cifrarioFlipped.get(messaggioCifrato)
        print('Il messaggio cifrato è:', messaggioCifratoStringa, '; il cui valore numerico è: ', messaggioCifrato)
        ripetere = input('Per arrestare il programma digita \'stop\', altrimenti premi un tasto. Scelta: ')
def decrittografaMessaggio(cifrarioFlipped, stringaValueError):
    stringaValueError = stringaValueError
    disponibilitaChiavi = ''
    while disponibilitaChiavi != 's' and disponibilitaChiavi != 'n':
        disponibilitaChiavi = input('Si dispone delle chiavi di cifratura?\nScelta (s/n): ')
        disponibilitaChiavi = disponibilitaChiavi.lower()
    if disponibilitaChiavi == 'n':
        chiavePrivata(stringaValueError)
    if disponibilitaChiavi == 's':
        try:
            n = int(input('Inserire valore di n: '))
            pri = int(input('Inserire valore di pri: '))
        except ValueError:
            print(stringaValueError)
            os.system('exit')
    ripetere = ''
    while ripetere != 'stop':
        try:
            messaggio = int(input('Immetti messaggio da decifrare: '))
        except ValueError:
            print(stringaValueError)
            os.system('exit')
        messaggioDecrittografatoNum = (messaggio ** pri) % n
        messaggioDecrittografato = cifrarioFlipped.get(messaggioDecrittografatoNum)
        print('Il messaggio decrittografato è: ', messaggioDecrittografato)
        ripetere = input('Per arrestare il programma digita \'stop\', altrimenti premi un tasto. Scelta: ')


# MAIN


cifrario = {'a':1,
            'b':2,
            'c':3,
            'd':4,
            'e':5,
            'f':6,
            'g':7,
            'h':8,
            'i':9,
            'j':10,
            'k':11,
            'l':12,
            'm':13,
            'n':14,
            'o':15,
            'p':16,
            'q':17,
            'r':18,
            's':19,
            't':20,
            'u':21,
            'v':22,
            'w':23,
            'x':24,
            'y':25,
            'z':26,
            'A': 27,
            'B': 28,
            'C': 29,
            'D': 30,
            'E': 31,
            'F': 32,
            'G': 33,
            'H': 34,
            'I': 35,
            'J': 36,
            'K': 37,
            'L': 38,
            'M': 39,
            'N': 40,
            'O': 41,
            'P': 42,
            'Q': 43,
            'R': 44,
            'S': 45,
            'T': 46,
            'U': 47,
            'V': 48,
            'W': 49,
            'X': 50,
            'Y': 51,
            'Z': 52
            }
cifrarioFlipped = {1:'a',
2:'b',
3:'c',
4:'d',
5:'e',
6:'f',
7:'g',
8:'h',
9:'i',
10:'j',
11:'k',
12:'l',
13:'m',
14:'n',
15:'o',
16:'p',
17:'q',
18:'r',
19:'s',
20:'t',
21:'u',
22:'v',
23:'w',
24:'x',
25:'y',
26:'z',
27:'A',
28:'B',
29:'C',
30:'D',
31:'E',
32:'F',
33:'G',
34:'H',
35:'I',
36:'J',
37:'K',
38:'L',
39:'M',
40:'N',
41:'O',
42:'P',
43:'Q',
44:'R',
45:'S',
46:'T',
47:'U',
48:'V',
49:'W',
50:'X',
51:'Y',
52:'Z'
}
modalita = '0'
stringaValueError= 'Si è verificato: ValueError. Il formato dati immesso non è corretto.'
while modalita != '1' and modalita != '2' and modalita != '3':
    modalita = input('Immetti la modalità:\n1) calcolo chiavi;\n2) crittografa un messaggio;\n3) decrittografa un messaggio.\nScelta: ')
    if modalita == '1':
        calcoloChiavi(stringaValueError)
    elif modalita == '2':
        crittografaMessaggio(cifrario, stringaValueError, cifrarioFlipped)
    elif modalita == '3':
        decrittografaMessaggio(cifrarioFlipped, stringaValueError)
    else:
        print('Riprova.')
