// Even Fibonacci numbers

#include <stdio.h>
#include <string.h>
#include<math.h>

int solve();

int main() {
    printf("%d\n", solve());
    return 0;
}

int solve() {
    long x = 600851475143;
    long i = 2;
    while (i < x) {
        if (x % i == 0) x /= i;
        else i++;
    }
    return i;
}
