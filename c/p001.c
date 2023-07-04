// Multiples of 3 and 5

#include <stdio.h>

int solve();

int main() {
    printf("%d\n", solve());
    return 0;
}

int solve() {
    int sum = 0;
    for (int i = 0; i < 1000; i++) {
        if (i % 3 == 0 || i % 5 == 0) sum += i;
    }
    return sum;
}
