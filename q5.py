x= int(input("Enter a number of repetitions"))

def repeatHello(func):
    def repeat():
        for i in range(x):
            func()
    return repeat
@repeatHello
def hello():
        print ('Hello')
        
hello()
