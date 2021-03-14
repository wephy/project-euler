# Number letter counts

below10 = [
           ['0', 0], ['1', 3], ['2', 3], ['3', 5], ['4', 4], 
           ['5', 4], ['6', 3], ['7', 5], ['8', 5], ['9', 4]
          ]

teens = [
         ['10', 3], ['11', 6], ['12', 6], ['13', 8], ['14', 8],
         ['15', 7], ['16', 7], ['17', 9], ['18', 8], ['19', 8]
        ]

above20 = [
           ['2', len('twenty')], ['3', len('thirty')], ['4', len('forty')], 
           ['5', len('fifty')], ['6', len('sixty')], ['7', len('seventy')], 
           ['8', len('eighty')], ['9', len('ninety')]
          ]

hundred_and = 10
hundred = 7

thousand = [['1000', len('onethousand')]]

total = 0
for i in range(1,1000+1):
    i = str(i)

    for n, l in thousand:
        if i == n:
            total += l

    last2 = str(int(i[-2:]))
    
    if int(last2) < 20:
        for n, l in below10:
            if last2 == n:
                total += l
        for n, l in teens:
            if last2 == n:
                total += l
    else:
        for n, l in above20:
            if last2[:1] == n:
                total += l
        for n, l in below10:
            if last2[-1:] == n:
                total += l
    
    if len(i) == 3:
        third = i[-3:-2]
        for n, l in below10:
            if third == n:
                total += l
                if int(i[-2:]) == 0:
                    total += hundred
                else:
                    total += hundred_and

print(total)
