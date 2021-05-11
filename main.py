import os
from math import gcd as mcm
# pub * priv = k * z + 1

def calcoloChiavi(n, pub, pri, stringValueError):
    try:
        a = int(input('Immettere valore di a: '))
        b = int(input('Immettere valore di b: '))
    except ValueError:
        print(stringaValueError)
        os.system('exit')
    n = a * b
    z = (a - 1) * (b - 1)
    pri = calcoloPri(z)
    print('# La chiave pubblica è: (', pub, ', ', n, ').\n# La chiave privata è: (', pri, ', ', n, ').')
def calcoloPri(z):
    controlloCiclo = False
    while controlloCiclo == False:
        k = 0
        priCalcolo = (((k * z) + 1) / pub)
        if isinstance(priCalcolo, int) == True:
            controlloCiclo = True
        else:
            k = k + 1
    return priCalcolo
def crittografaMessaggio(cifrario, stringaValueError, n, pub, pri):
    disponibilitaChiavi = ''
    while disponibilitaChiavi != 's' and disponibilitaChiavi != 'n':
        disponibilitaChiavi = input('Si dispone delle chiavi di cifratura?\nScelta (s/n): ')
        disponibilitaChiavi = disponibilitaChiavi.lower()
    if disponibilitaChiavi == 'n':
        calcoloChiavi(n, pub, pri)
    if disponibilitaChiavi == 's':
        try:
            pub = int(input('Inserire valore di pub: '))
            n = int(input('Inserire valore di n: '))
            pri = int(input('Inserire valore di pri: '))
        except ValueError:
            print(stringaValueError)
            os.system('exit')
    ripetere = ''
    while ripetere != 'stop':
        messaggio = input('Inserisci il valore da cifrare: ')
        messaggio = messaggio.lower()
        # elevamento a potenza: x ** y
        messaggioCifrato = cifrario[messaggio]
        messaggioCifrato = (messaggioCifrato ** pub) % n
        print('Il messaggio cifrato è: ', messaggioCifrato)
        ripetere = input('Per arrestare il programma digita \'stop\', altrimenti premi un tasto. Scelta: ')
def decrittografaMessaggio(cifrario, stringaValueError, n, pub, pri):
    disponibilitaChiavi = ''
    while disponibilitaChiavi != 's' and disponibilitaChiavi != 'n':
        disponibilitaChiavi = input('Si dispone delle chiavi di cifratura?\nScelta (s/n): ')
        disponibilitaChiavi = disponibilitaChiavi.lower()
    if disponibilitaChiavi == 'n':
        calcoloChiavi(n, pub, pri)
    if disponibilitaChiavi == 's':
        try:
            pub = int(input('Inserire valore di pub: '))
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
        messaggioDecrittografato = (messaggio ** pri) % n
        for i in cifrario:
            if (cifrario[i] == messaggioDecrittografato):
                print('Il messaggio decrittografato è: ', i)
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
            'z':26}
modalita = '0'
n = 0
pub = 0
pri = 0
stringaValueError= 'Si è verificato: ValueError. Il formato dati immesso non è corretto.'
while modalita != '1' and modalita != '2' and modalita != '3':
    modalita = input('Immetti la modalità:\n1) calcolo chiavi;\n2) crittografa un messaggio;\n3) decrittografa un messaggio.\nScelta: ')
    if modalita == '1':
        calcoloChiavi(n, pub, pri, stringaValueError)
    elif modalita == '2':
        crittografaMessaggio(cifrario, stringaValueError, n, pub, pri)
    elif modalita == '3':
        decrittografaMessaggio(cifrario, stringaValueError, n, pub, pri)
    else:
        print('Riprova.')
