#Напишите программу,
# выполняющую различные вычисления и  выводящую  значений с применение методов форматирования, манипуляторов и флагов объекта cout.
x = int(input("x: "))
y = int(input("y: "))

z = x * y

product = ('Умножили : {}'.format(z))


print('Первая буква Умножили будет с маленькой ----',product.lower())
print('БУДЕТ НАПИСАНО КАПСОМ ----',product.upper())
print('С заглавной ----',product.title())