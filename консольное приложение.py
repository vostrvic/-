x = int(input())
maximum = 0
for i in range(x, -1, -1):
    number = str(i)
    current_sum = sum(int(digit) for digit in number)
    if current_sum > maximum:
        maximum = current_sum
        best_number = i
print("Максимальное значение суммы цифр:", maximum)
print("Соответствующее число:", best_number)