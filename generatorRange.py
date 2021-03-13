def rangeGenrator():
    rangeVariable = range(1,6)
    for variable in rangeVariable:
        yield variable


generatorOutput = rangeGenrator()

for randomNumber in generatorOutput:
    print(randomNumber)