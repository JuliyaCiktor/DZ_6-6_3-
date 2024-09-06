num = int(input("Введите число: "))
while num > 9:
    product = 1
    for digit in str(num):
        product *= int(digit)
    num = product
print("Результат:", num)
