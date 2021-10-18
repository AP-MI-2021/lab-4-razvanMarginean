def meniu():
    print("1.Citire lista")
    print("2.Afisare lista dupa eliminarea numere prime din lista")


def citireLista(l):
    l = []
    givenString = input('Dati elemente lista separate prin virgula:')
    numbersAssString = givenString.split(",")
    for x in numbersAssString:
        l.append(int(x))
    return l

def Test():
    TesteliminareNumerePrime()

def eliminareNumerePrime(l):
    '''
    Elimina numerele prime din lista
    :param l: lista cu nr de tip int
    :return: returneaza lista dupa eloiminarea nr prime
    '''
    rezultat = []
    for x in l:
        ok = True
        if x < 2:
            ok = False
        for i in range(2, x//2+1):
            if x % i == 0:
                ok = False
        if ok == False:
            rezultat.append(x)
    return rezultat


def TesteliminareNumerePrime():
    assert eliminareNumerePrime([8, 19, 17, 25]) == [8, 25]

def main():
    TesteliminareNumerePrime()
    Test()
    l = []
    while True:
        meniu()
        optiune = input("Selectati optiune:")
        if optiune == '1':
            l = citireLista(l)
        elif optiune == '2':
            print(eliminareNumerePrime(l))
        elif optiune == '6':
            break
main()
