test = 7
numCar = 3


def numero(num,nbreCaracteres):
    chaineNum = str(num)
    while len(chaineNum) < nbreCaracteres:
        chaineNum = "0" + chaineNum
    return chaineNum


print(numero(test,numCar))
