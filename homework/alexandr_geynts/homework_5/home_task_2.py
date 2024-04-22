results = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9"
]

result_1 = int(results[0].split(":")[-1].strip()) + 10
result_2 = int(results[1].split(":")[-1].strip()) + 10
result_3 = int(results[2].split(":")[-1].strip()) + 10

print("Результат 1:", result_1)
print("Результат 2:", result_2)
print("Результат 3:", result_3)
