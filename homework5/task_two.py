user_index = int(input("Enter number: "))
a = 0
b = 1
index = 1
while True:
    index += 1
    new_number = a + b
    print(index, new_number)
    a = b
    b = new_number
    if user_index == index:
        print(f"Результат: Число Фибоначчи = {new_number}")
        break
