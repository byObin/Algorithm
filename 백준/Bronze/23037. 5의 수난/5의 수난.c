#include <stdio.h>
#include <math.h>

int main(){
    int num[5];
    int sum = 0;
    
    for (int i = 0; i < 5; i++){
        scanf("%1d", &num[i]);
        sum += pow(num[i], 5);
    }
    
    printf("%d", sum);
    
    return 0;
}