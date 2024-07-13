#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	int i = 0;
	int size[6] = { 0 ,};
	while (i < 6 && scanf("%d", &size[i]) == 1) {
		i++;
	}
	int t;
	int p;
	scanf("%d %d", &t, &p);
	
	int t_cnt = 0;
	for (int j = 0; j < 6; j++) {
		if (0 < size[j] && size[j] <= t) {
			t_cnt++;
		}
		else {
			t_cnt += (size[j] / t) + ((size[j]%t) != 0 ? 1 : 0);
		}
	}

	printf("%d\n", t_cnt);
	printf("%d %d\n", n / p, n % p);
	
	return 0;
}