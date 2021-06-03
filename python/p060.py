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

print(sum(min([i for i in find_cliques(G) if len(i) == 5])))
