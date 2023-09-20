b=int(input('Number'))
def division(b):
    try:
        a = 10 / b
        print(a)
        print('try completed')
    except ZeroDivisionError:
        print('cant divided by 0')
        b = int(input("enter a non zero number"))
        division(b)
division(b)
print('program completed')
