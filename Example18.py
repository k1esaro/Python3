import random
lenght =int(input("Введите кол-во эллементов списка: "))
list = []
while len(list) <lenght:
    list.append(int(random.randint(1, 10)))
print(list)
x=int(input('Введите значения х: '))
i=0
output = list[0]
dif=list[0]
while i < len(list):
    if abs(list[i]-x) < dif:
        dif=abs(x-list[i])
        output= list[i]
        i+=1
    else:
        i+=1
print("Самое близкое к x:", output)