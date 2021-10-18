l = [1, 2, 3, 4, 5, 6]

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
print(l)
print(eliminareNumerePrime(l))