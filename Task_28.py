def recSum(a, b):
    if b == 0:
        return a
    return 1 + recSum(a, b - 1)
numberA = int(input("Введите целое неотрицательное число: "))
numberB = int(input("Введите еще одно целое неотрицательное число: "))
print(f"{recSum(numberA, numberB)}")