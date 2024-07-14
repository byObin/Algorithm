#include <stdio.h>

int main() {
	int a, b;
	int num[1000];
	int idx = 0;
	int result = 0;

	scanf("%d %d", &a, &b);

	
	for (int i = 1; i < 1000; i++) {
		for (int j = 0; j < i; j++) {
			if (idx == 1000) {
				break;
			}
			num[idx] = i;
			idx++;
		}
	}


	for (int i = a - 1; i < b; i++) {
		result += num[i];
	}

	printf("%d", result);
	
}