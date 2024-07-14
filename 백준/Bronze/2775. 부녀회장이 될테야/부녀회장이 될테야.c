#include <stdio.h>

int main() {
	int t;
	int apt[15][15];
	int k, n;

	for (int i = 1; i < 15; i++) {
		apt[0][i] = i;
		apt[i][1] = 1;
	}

	for (int i = 1; i < 15; i++) {
		for (int j = 1; j < 14; j++) {
			apt[i][j+1] = apt[i][j] + apt[i - 1][j+1];
		}
	}

	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		scanf("%d", &k);
		scanf("%d", &n);

		printf("%d\n", apt[k][n]);
	}
}