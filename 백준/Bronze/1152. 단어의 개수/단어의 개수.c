#include <stdio.h>

int main() {
	char S[1000000];
	gets(S);
	int count = 0;
	int k = 0;
	if (S[0] != ' ') {
		count++;
	}
	while (S[k]) {
		if (S[k] == ' ' && S[k+1]!='\0') {
			count++;
		}
		k++;
	}
	printf("%d", count);
}