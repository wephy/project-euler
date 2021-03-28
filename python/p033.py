# Digit cancelling fractions

digit_cancelling_fractions = []
for top in range(11, 100):
    if str(top)[1] != '0':
        for bot in range(top, 100):
            if (str(bot)[1] != '0' and top != bot):
                if (
                    (top/bot == int(str(top)[0]) / int(str(bot)[1])
                     and str(top)[1] == str(bot)[0])
                    or
                    (top/bot == int(str(top)[1]) / int(str(bot)[0])
                     and str(top)[0] == str(bot)[1])
                     ):

                    digit_cancelling_fractions.append([top, bot])

a, b = 1, 1
for fraction in digit_cancelling_fractions:
    a *= fraction[0]
    b *= fraction[1]

d = b
while b:
    a, b = b, a % b
print(d // a)
