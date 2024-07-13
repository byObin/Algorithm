#include <stdio.h>

int main(){
    int n, k;
    int num[1001];
    
    scanf("%d %d", &n, &k);
    
    for (int i=0; i<n; i++){
        scanf("%d", &num[i]);
    }
    
    for (int i=0; i<n-1; i++){
        for (int j=i+1; j<n; j++){
            if (num[i] > num[j]){
                int tmp = num[j];
                num[j] = num[i];
                num[i] = tmp;
            }
        }
    }
    
    printf("%d\n", num[n-k]);
    
    return 0;
}