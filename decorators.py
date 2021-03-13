def giveTitles(func):
    def wrapper():
        data = func()
        for personData in data:
            if str(personData[2]).lower() == "m" or "male":
                print("Mr. ", personData[0])
            else:
                print("Ms. ", personData[0])
    return wrapper


def standardizeMobile(func):
    def wrapper():
        mobileNumber = func()
        print("+91",mobileNumber[-10:])
    return wrapper
