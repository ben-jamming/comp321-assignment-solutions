#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int main() {
    uint64_t line;
    int i, first;

    char output[1024]; // Large enough to hold the output string
    char *ptr; // Pointer used for concatenation

    while (1) {
        if (scanf("%lu", &line) != 1) break;
        if (line == 0) break;

        line--;
        ptr = output;
        ptr += sprintf(ptr, "{");
        first = 1;

        for (i = 0; i < 64 && line > 0; line >>= 1, i++) {
            if (line & 1) {
                if (!first) {
                    ptr += sprintf(ptr, ", ");
                }

                uint64_t power = 1;
                for (int j = 0; j < i; ++j) {
                    power *= 3;
                }
                ptr += sprintf(ptr, " %lu", power);
                first = 0;
            }
        }

        sprintf(ptr, " }");
        printf("%s\n", output); // Print the whole string
    }

    return 0;
}