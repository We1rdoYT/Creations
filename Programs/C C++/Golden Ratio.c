#include <stdio.h>
#include <math.h>

float phi(float F) {
    return 1 + 1 / F;
}

int main() {
    const float PHI = (1 + sqrtf(5)) / 2;

    float F;

    printf("Phi = 1 + (1 / Phi) = %f\nF = ", PHI);
    scanf("%f", &F);
    
    while (F != PHI)
    {
        printf("Phi = 1 + (1 / %f) = ", F);

        F = phi(F);
        printf("%f\n", F);
    }

    printf("%f, Phi calculated!", F);

    return 0;
}
