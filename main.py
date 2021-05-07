import os
import itertools

def calcoloChiavi():
    a = input('Immettere valore di a: ')
    b = input('Immettere valore di b: ')
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print('Si è verificato: ValueError. Almeno uno dei due input non corrisponde ad un intero.')
        os.system('exit')
    n = a * b
    z = (a - 1) * (b - 1)
    pri = calcoloPri(z)
    q = trovaQ(z, pri)
    pub = (((q * z) + 1) / pri)
    print('Le chiavi sono: (', pub, ', ', n, ') & (', pri, ', ', n, ').')
def calcoloPri(z):
    numeriPrimi = [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in numeriPrimi:
        if z % i != 0:
            return i
            break
def trovaQ(z, pri):
    for i in range(100):
        temp = (((i * z) + 1) / pri)
        controllo = isinstance(temp, int)
        if controllo == True:
            return i
            break
def crittografaMessaggio():
    pass
def decrittografaMessaggio():
    pass

# MAIN

modalita = '0'
while modalita != '1' and modalita != '2' and modalita != '3':
    modalita = input('Immetti la modalità:\n1) calcolo chiavi;\n2) crittografa un messaggio;\n3) decrittografa un messaggio.\nScelta: ')
    if modalita == '1':
        calcoloChiavi()
    elif modalita == '2':
        crittografaMessaggio()
    elif modalita == '3':
        decrittografaMessaggio()
    else:
        print('Riprova')
