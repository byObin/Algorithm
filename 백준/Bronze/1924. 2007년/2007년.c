#include <stdio.h>

int main() {
	int x, y;
	int months[12] = { 31,28,31,30,31,30,31,31,30,31,30,31 };
	char days[7][4] = { "MON", "TUE", "WED","THU","FRI","SAT","SUN"};

	scanf("%d %d", &x, &y);

	int time = 0;
	for (int i = 0; i < x-1 ; i++) {
		time += months[i];
	}

	printf("%s\n", days[(time+y-1)%7]);
}