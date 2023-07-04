// Even Fibonacci numbers

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<math.h>

int solve();

int main() {
   printf("%d\n", solve());
   return 0;
}

int solve() {
    int answer = 0;
    for (int i = 100; i < 1000; i++) {
        for (int j = i; j < 1000; j++) {
            int x = i * j;
            if (x < answer) break;
            int size = snprintf(NULL, 0, "%d", x);
            char* str = malloc(size + 1);
            char* reversed = malloc(size + 1);
            snprintf(str, size + 1, "%d", x);
            int len = strlen(str);
            for (int k = 0; k < len; k++) {
                reversed[len - k - 1] = str[k];
            }
            if (strcmp(str, reversed) == 0) answer = x;
        }
    }
    return answer;
}
