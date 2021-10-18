l = [25, 13, 26, 13]
def TestPrelucareListaTuplu(l):
    rezultat = []
    indice = -1
    for x in l:
        count = l.count(x)
        indice = indice + 1
        rezultat.append(x)
        rezultat.append(indice)
        rezultat.append(count)
    return rezultat
print(TestPrelucareListaTuplu(l))