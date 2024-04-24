results = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9"
]

result1 = results[0]
result2 = results[1]
result3 = results[2]

result_1 = int(result1[result1.index(':') + 2:]) + 10
result_2 = int(result2[result2.index(':') + 2:]) + 10
result_3 = int(result3[result3.index(':') + 2:]) + 10

print("Результат 1:", result_1)
print("Результат 2:", result_2)
print("Результат 3:", result_3)
