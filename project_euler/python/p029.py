# Distinct powers

sequence = []

for a in range(2, 101):
    for b in range(2, 101):
        term = a ** b
        if term not in sequence:
            sequence.append(term)

print(len(sequence))
