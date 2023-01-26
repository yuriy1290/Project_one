numberone = float(input("numberone = "))
numbertwo = float(input("numbertwo = "))
count = int(input("Count actions: "))
while (count != 0):
    count -= 1
    action = int(input("Выберите действие которое хотите сделать:\n"
    "Сложить: 1\n"
    "Вычесть: 2\n"
    "Умножить: 3\n"
    "Поделить: 4\n"
    "Действие: "))
    if action == 1:
        numberone = numberone + numbertwo
    if action == 2:
        numberone = numberone - numbertwo
    if action == 3:
        numberone = numberone * numbertwo
    if action == 4:
        if numbertwo != 0:
           numberone = numberone / numbertwo
        else: 
            print("Делить на ноль ата-та!")
            numbertwo =  float(input("numbertwo again = "))
            numberone = numberone / numbertwo
    print(numberone)
    numbertwo =  float(input("numbertwo again = "))