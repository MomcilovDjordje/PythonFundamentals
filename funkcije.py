def mnozenje(c,b):
    izmnozeno= c*b
    return izmnozeno

x= int(input('enter a number: '))
if x == '':
    print('unesi broj')
b= int(input('enter a second number: '))
if b == '':
    print('unesi broj')

print("Rezultat je " + str(mnozenje(x,b)))




