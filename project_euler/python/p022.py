# Names scores

# Cleaning data
with open("P22_names.txt", "r") as data:
    namesData = data.readlines()
names = eval(namesData[0])

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

namesSorted = []
for name in names:
    namesSorted.append(name)
namesSorted.sort()


# Calculation
totalScore = 0

for name in namesSorted:
    valueAlphabetical = 0
    valuePosition = namesSorted.index(name)+1
    for letter in name:
        valueAlphabetical += letters.index(letter)+1
    totalScore += valueAlphabetical * valuePosition

print(totalScore)
