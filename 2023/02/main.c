#include "../types.h"
#include "../utils.h"
#include "../regex.h"


int main(int argc, char *argv[]) {
	int max_r = 12, max_g = 13, max_b = 14;

	FILE *file = fopen("data.txt", "r");
	ASSERT(file); // File failed to open
	int MAX_LINE_SIZE = 1024;
	
	regex_t* cregex = RE_compile(bstring_c("\\d+ \\w"));

	int answer1 = 0, answer2 = 0;
	int ln = 0;
	bstring line_buffer = bstring_alloc(MAX_LINE_SIZE);
	while (++ln, read_next_line(file, &line_buffer, MAX_LINE_SIZE)) {
		int r = 0, g = 0, b = 0;
		bstring m = line_buffer;
		while (RE_match(cregex, m, &m)) {
			int d = atoi((char*)m.head); // We're not null-terminated, but it's probably fine...
			switch (m.tail[-1]){
				case 'r': {
					r = (r > d) ? r : d;
				} break;
				case 'g': {
					g = (g > d) ? g : d;
				} break;
				case 'b': {
					b = (b > d) ? b : d;
				} break;
			}
			m.head = m.tail;
			m.tail = line_buffer.tail;
		}
		if(r <= max_r && g <= max_g && b <= max_b){
			answer1 += ln;
		}
		answer2 += r*g*b;
	}

	printf("answer1 = %d\n", answer1);
	printf("answer2 = %d\n", answer2);

	ASSERT(answer1 == 2512);
	ASSERT(answer2 == 67335);

	free(line_buffer.head);
	fclose(file);
	RE_free(cregex);

	return 0;
}
