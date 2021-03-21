# Names scores

# Cleaning data
with open("P22_names.txt", "r") as data:
    names_data = data.readlines()
names = eval(names_data[0])

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

names_sorted = []
for name in names:
    names_sorted.append(name)
names_sorted.sort()


# Calculation
total_score = 0

for name in names_sorted:
    value_alphabetical = 0
    value_position = names_sorted.index(name)+1
    for letter in name:
        value_alphabetical += letters.index(letter)+1
    total_score += value_alphabetical * value_position

print(total_score)
