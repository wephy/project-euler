# Pandigital products

def get_product_sets(num):
    return_list = []
    for multiplicand in range(2, int((num ** 0.5) + 1)):
        if num % multiplicand == 0:
            return_list.append([multiplicand, int(num / multiplicand)])
    return return_list


tests = []
for p in range(1000, 10000):
    p_string = str(p)
    running = True
    while running:
        if (p_string.count('0') > 0):
            running = False
        for d in range(1, 10):
            if (p_string.count(str(d))) > 1:
                running = False
        if running is True:
            tests.append(p)
            running = False

pandigital_products = []
for test in tests:
    m_sets = get_product_sets(test)

    for m_set in m_sets:
        if test in pandigital_products:
            continue

        m_string = ""
        m_string += str(m_set[0]) + str(m_set[1]) + str(test)

        running = True
        while running:
            if (m_string.count('0') > 0):
                running = False

            for d in range(1, 10):
                if (m_string.count(str(d))) == 1:
                    continue
                else:
                    running = False

            if running is True:
                pandigital_products.append(test)
                running = False

print(sum(pandigital_products))
