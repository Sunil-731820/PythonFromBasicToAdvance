def hello():
    print("Hello Welcome to this tutorials ")
hello()

def evenOrOdd(num):
    if num%2==0:
        print("the Number is Even Number")
    else:
        print("the Number is odd Number")
evenOrOdd(12)
evenOrOdd(11)
hello()


def studentName(firstName, lastName):
    print(firstName , lastName)
studentName(firstName="Sunil Kumar" , lastName="gupta")


def myfunc(*argv):
    for arg in argv:
        print(arg)
myfunc("This ","is ","Sunil ","Kumar,","gupta")


def squareNumber(num):
    return  num**2
print(squareNumber(12))
print("the square of the Number is ")
print(squareNumber(200))



