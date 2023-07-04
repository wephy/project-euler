// Even Fibonacci numbers

#include <stdio.h>
#include <string.h>
#include <math.h>

int LIMIT = 4000000;
int solve();
int fibonacci();

int main() {
    printf("%d\n", solve());
    return 0;
}

int solve() {
    int fibs = (ceil(log(LIMIT * pow(5, 0.5)) / log(0.5 * (1 + pow(5, 0.5)))));
    int table[fibs];
    memset(table, 0, sizeof(table));
    int sum = 0;

    for (int i = 1; i < fibs; i += 3) {
        int x = fibonacci(i, table);
        if (x < LIMIT) sum += x;
    }
    return sum;
}

int fibonacci(int n, int table[]) {
    if (n == 0) table[0] = 1;
    if (n == 1) table[1] = 2;
    if (table[n] != 0) return table[n];
    table[n] = fibonacci(n - 1, table) + fibonacci(n - 2, table);
    return table[n];
}
