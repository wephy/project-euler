# Champernowne's constant

digit_sections = {0: 0}
current = 1
while digit_sections[current-1] < 1_000_000:
    digit_sections[current] = (digit_sections[current-1] +
                               (9 * (10 ** (current - 1)) * current))
    current += 1


def digit_finder(nth_digit):
    digit = 0
    for section in digit_sections:
        if digit_sections[section] >= nth_digit:
            number_of_digits = section
            position_index = nth_digit - digit_sections[section-1]
            div, mod = divmod(position_index, number_of_digits)
            if mod > 0:
                div += 1
            digit_index = mod
            if digit_index == 0:
                digit_index = number_of_digits
            parent_number = div + ((10 ** (number_of_digits-1)) - 1)
            parent_number_str = str(parent_number)
            digit = parent_number_str[digit_index-1]
            break
    return int(digit)


answer = 1
for i in range(7):
    digit_n = (10 ** i)
    answer *= digit_finder(digit_n)
print(answer)
