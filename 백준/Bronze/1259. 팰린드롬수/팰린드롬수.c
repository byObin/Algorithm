#include <stdio.h>
#include <string.h>

int main() {
	char n[1000000];
	while (1) {
		int isPal = 1;
		scanf("%s", n);

		int len = strlen(n);

		if (len == 1 && n[0] == '0') {
			break;
		}

		for (int i = 0; i < (len / 2); i++) {
			if (n[i] != n[len - 1 - i]) {
				isPal = 0;
				break;
			}
		}
		
		if (isPal) {
			printf("yes\n");
		}
		else {
			printf("no\n");
		}
	}
}