import random
lenght =int(input("Введите кол-во эллементов списка: "))
list = []
while len(list) <lenght:
    list.append(int(random.randint(1, 10)))
print(list)
x=int(input('Введите значения х: '))
i=0
output=0
while i<len(list):
    if x==list[i]:
        output+=1
        i+=1
    else:
        i+=1
print('Встречается ',output," раз(а)")