l = [19, 5, 24, 12, 9, 2]
def PrelucrareLista(l):
    '''
    Adauga dupa fiecare numar, numarul divizorilor sai
    :param l:lista de int-uri
    :return:Lista
    '''
    rezultat = []
    for x in l:
        nrd = 0
        for i in range(2, x//2+1):
            if x % i == 0:
                nrd = nrd + 1
        rezultat.append(x)
        rezultat.append(nrd)
    return rezultat
print(PrelucrareLista(l))
