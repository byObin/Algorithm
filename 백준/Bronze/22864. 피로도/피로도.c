#include <stdio.h>

int main() {
	int a, b, c, m;
	scanf("%d %d %d %d", &a, &b, &c, &m);
	int work = 0;
	int time = 0;
	int stress = 0;
	while (time < 24 && m >= stress) {
		if ((stress + a) <= m) {
			work += b;
			stress += a;
		}
		else {
			stress -= c;
			if (stress < 0) {
				stress = 0;
			}
		}
		time++;
	}
	printf("%d", work);
	
	return 0;
}