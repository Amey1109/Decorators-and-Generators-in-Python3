from decorators import giveTitles
@giveTitles
def getData():
    numberOfPeople = int(input("Enter the total Number of people? "))
    peopleData = []
    for inputs in range(numberOfPeople):
        person = []
        name = str(input("Enter Name: "))
        age = int(input("Enter Age: "))
        sex = str(input("Enter sex either 'M' or 'F': "))
        print("\n")
        person.append(name)
        person.append(age)
        person.append(sex)
        peopleData.append(tuple(person))

    peopleData.sort(key=lambda x: x[1])
    return peopleData

getData()