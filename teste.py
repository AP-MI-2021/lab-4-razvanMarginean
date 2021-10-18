l = [1, 2, 3, 4]
def MedieAritmetica(l):
    '''
    Calculeaza media aritmetica a numerelor din lista
    :param l: lista de int-uri
    :return: valoarea mediei aritmetice
    '''
    rezultat = 0
    for x in l:
        rezultat = rezultat + x
    rezultat = rezultat // len(l)
    return rezultat

print(MedieAritmetica(l))
