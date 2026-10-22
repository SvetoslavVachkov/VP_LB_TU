import random

length = int(input("Size: "))

numbers = [random.randint(1, 10) for i in range(length)]
print("List:", numbers)

result_list = []

for i in range(len(numbers) - 1):
    result_list.append(numbers[i])
    result_list.append(numbers[i] + numbers[i + 1])

if numbers:
    result_list.append(numbers[-1])

print("Result list:", result_list)