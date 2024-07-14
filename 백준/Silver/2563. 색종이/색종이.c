#include <stdio.h>

int main() {
	int n;
	int paper[100][100] = { 0, };
	int x;
	int y;
	int sum = 0;

	scanf("%d", &n);

	for (int k = 0; k < n; k++) {
		scanf("%d %d", &x, &y);

		for (int dx = 0; dx < 10; dx++) {
			for (int dy = 0; dy < 10; dy++) {
				paper[x + dx][y + dy] = 1;
			}
		}
	}
	
	for (int i = 0; i < 100; i++) {
		for (int j = 0; j < 100; j++) {
			if (paper[i][j] == 1) {
				sum++;
			}
		}
	}

	printf("%d", sum);

	return 0;
}