#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
	char s[1000001];
	
	scanf("%s", s);
	
	int len = strlen(s);
	int cnt[26] = { 0, };

	for (int i = 0; i < len; i++) {
		if (isalpha(s[i])) {
			cnt[toupper(s[i])-'A']++;
		}
	}

	int max = cnt[0];
	int idx = 0;
	for (int i = 0; i < 26; i++) {
		if (cnt[i] > max) {
			max = cnt[i];
			idx = i;
		}
	}

	int max_cnt = 0;
	for (int i = 0; i < 26; i++) {
		if (cnt[i] == max) {
			max_cnt++;
		}
	}

	if (max_cnt > 1) {
		printf("?\n");
	}
	else {
		printf("%c", idx + 'A');
	}
}