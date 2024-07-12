#include <stdio.h>
#include <stdlib.h>

int main(){
    int n;
    scanf("%d", &n);
    
    int* num = (int*)malloc(n * sizeof(int));
    
    for(int i = 0; i < n; i++){
        scanf("%d", &num[i]);
    }
    
    int min = num[0];
    int max = num[0];
    
    for(int i = 1; i < n; i++){
        if (num[i] < min){
            min = num[i];
        }
        
        if (num[i] > max){
            max = num[i];
        }
    }
    
    printf("%d %d", min, max);
    
    free(num);
    return 0;
}