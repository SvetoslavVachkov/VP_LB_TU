u_input = input("Number: ")

digits = [int(char) for char in u_input if char.isdigit()]

f_tuple = tuple(sorted(digits))
r_tuple = tuple(reversed(digits))

print(f_tuple)
print(r_tuple)