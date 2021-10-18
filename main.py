def meniu():
    print("1.Citire lista")
    print("2.Afisare lista dupa eliminarea numere prime din lista")
    print("3.Evaluare daca media aritmetica a numerelor din lista este mai mare decat un nr k dat")
    
    print("6.Iesire")

def citireLista(l):
    l = []
    givenString = input('Dati elemente lista separate prin virgula:')
    numbersAssString = givenString.split(",")
    for x in numbersAssString:
        l.append(int(x))
    return l

def Test():
    TestMedieAritmetica()
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

def MedieAritmetica(l):
    '''
    Calculeaza media aritmetica a numerelor din lista
    :param l: lista de int-uri
    :return: valoarea mediei aritmetice
    '''
    rezultat = 0
    for x in l:
        rezultat = rezultat + x
    rezultat = rezultat // int(len(l))
    return rezultat


def TestMedieAritmetica():
    assert MedieAritmetica([1, 2, 3, 4]) == 2
    assert MedieAritmetica([10, -3, 25, -1, 3, 25, 18]) == 11


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
        elif optiune == '3':
            k = int(input("Dati valoare numar pt k:"))
            if k > MedieAritmetica(l):
                print("NU")
            else:
                print("DA")
        elif optiune == '6':
            break
main()
