# Digit cancelling fractions

digit_cancelling_fractions = []
for numerator in range(11, 100):
    if str(numerator)[1] != '0':
        for denominator in range(numerator, 100):
            if (str(denominator)[1] != '0'
                and numerator != denominator):
                if (numerator/denominator == int(str(numerator)[0]) / int(str(denominator)[1])
                    and str(numerator)[1] == str(denominator)[0]
                or
                    numerator/denominator == int(str(numerator)[1]) / int(str(denominator)[0]) 
                    and str(numerator)[0] == str(denominator)[1]):
                    digit_cancelling_fractions.append([numerator, denominator])

numerator_answer, denominator_answer = 1, 1
for fraction in digit_cancelling_fractions:
    numerator_answer *= fraction[0]
    denominator_answer *= fraction[1]

a, b = numerator_answer, denominator_answer
while b:
    a, b = b, a % b
print(denominator_answer // a)
