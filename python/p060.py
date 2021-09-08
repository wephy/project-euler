# Prime pair sets

import networkx as nx
from networkx.algorithms.clique import find_cliques
from sympy import isprime, nextprime

G = nx.Graph()

primes = set()
n = 2
while max([0] + [len(i) for i in find_cliques(G)]) < 5:
    n = nextprime(n)
    G.add_node(n)
    primes.add(n)

    for p in primes:
        if all(isprime(int(i)) for i in [f"{p}{n}", f"{n}{p}"]):
            G.add_edge(p, n)
print("Done")


    print(sum(min([i for i in find_cliques(G) if len(i) == 5])))

# from sympy import sieve, isprime

# primes = sieve.primerange(30_000)

# # Assuming `primes' is a sufficiently big, ordered list of primes
# # Assuming `is_prime()' is a primality test (e.g. Miller-Rabin)
# size = 5 # length of the desired solution
# it = iter(primes)

# q = [[]] # queue containing partial, compatible subsets of primes
# while q:
#   p = next(it) # get next prime in list
#   y = str(p)   # convert to string
#   for i in range(len(q)): # q[i] compatible subset
#     if all(isprime(int(x + y)) and isprime(int(y + x)) for x in q[i]):  # prime is compatible with q[i]
#       t = q[i] + [y] # add the prime to a copy of that subset

#       if len(t) == size:  # desired size achieved
#         print(' + '.join(t), '=', sum(int(x) for x in t))

#       elif len(t) < size:
#         q.append(t) # append the new compatible subset to the queue