# Arranged probability

from math import ceil, floor
from decimal import Decimal

FACTOR = Decimal(0.7071067811865475244008443)

UPPER = Decimal(0.7071067811866)
LOWER = Decimal(0.7071067811864)

blue_disk_solutions = []
# numerator = 7071067811865

numerator = 7071078394496

while len(blue_disk_solutions) < 1:

    # print(numerator)
    denominator_lower = ceil(numerator / Decimal(UPPER) - numerator)
    denominator_upper = floor(numerator / Decimal(LOWER) - numerator)

    for denominator in range(denominator_lower, denominator_upper):
        # print(denominator)
        # print(numerator, denominator)
        if (
            (2 * (numerator * (numerator-1)) == ((numerator+denominator) * (numerator+denominator-1)) )
        ):
            blue_disk_solutions.append(numerator)
            print(numerator, denominator, numerator+denominator)

    numerator += 1

print(blue_disk_solutions)