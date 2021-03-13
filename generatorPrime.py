def generatorPrime():
    for number in range(0,21):
        if number>1:
            for divisor in range(2,number):
                if number% divisor == 0:
                    break
            else:
                yield number

for primeNumber in generatorPrime():
    print(primeNumber)