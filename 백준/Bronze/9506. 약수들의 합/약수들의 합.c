#include <stdio.h>

int main() {
	while (1) {
		int n;
		int nums[100000];
		int idx = 0;
		int sum = 0;

		scanf("%d", &n);

		if (n == -1) {
			break;
		}

		for (int i = 1; i < n; i++) {
			int is_in_ar = 0;
			if (n % i == 0) {
				for (int k = 0; k < idx; k++) {
					if (nums[k] == i) {
						is_in_ar = 1;
					}
				}
				if (!is_in_ar) {
					nums[idx] = i;
					idx++;
				}
			}
		}

		for (int i = 0; i < idx; i++) {
			sum += nums[i];
		}

		if (n == sum) {
			printf("%d = ", n);
			for (int i = 0; i < idx - 1; i++) {
				printf("%d + ", nums[i]);
			}
			printf("%d\n", nums[idx - 1]);
		}
		else {
			printf("%d is NOT perfect.\n", n);
		}
	}
}