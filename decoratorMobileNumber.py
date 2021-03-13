from decorators import standardizeMobile
@standardizeMobile
def getMobileNumber():
    number = str(input("Enter your mobile number: "))
    return number

getMobileNumber()