n = int(input("Integer: "))

numbers = list(range(1, n + 1))

reversed_numbers = numbers[::-1]

result_dict = {numbers[i]: reversed_numbers[i] for i in range(len(numbers))}

print("List:", numbers)
print("Dictionary:", result_dict)