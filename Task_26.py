def degreeNumbers(a, b):
    if b == 0:
        return 1
    return a * degreeNumbers(a, b - 1)
number = int(input("Введите число: "))
degree = int(input("Введите степень: "))
print(f"{degreeNumbers(number, degree)}")