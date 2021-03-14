
# Double-base palindromes

db_palindromes = []

for num in range(1, 1000000):
    num_string = str(num)
    num_binary = bin(num)
    num_binary_string = str(num_binary[2:])
    if (num_string == num_string[::-1]) and (
        num_binary_string == num_binary_string[::-1]):
        db_palindromes.append(num)

print(sum(db_palindromes))