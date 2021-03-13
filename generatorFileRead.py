def generatorFileRead():
    with open("test.txt") as file:
        yield file.read()

for data in generatorFileRead():
    print(data,end=' ')