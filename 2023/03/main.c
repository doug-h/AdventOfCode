#include "../types.h"
#include "../utils.h"
#include "../regex.h"

#define LINE_SIZE 140


int add_symbols(bstring* prev, bstring* line, bstring* next){
	int value = 0;
	bstring number = *line;
	while (RE_matchp(bstring_c("\\d+"), number, &number)) {
		// Number valid if there are any nearby symbols
		int d = 0;

		size start = number.head - line->head;
		size end   = line->tail - number.tail;

		bstring* lines[3] = {prev, line, next};
		for(int i=0; i<3; ++i){
			if(lines[i] && !d) {
				for(u8* s = lines[i]->head+max(start-1,0); s<lines[i]->tail-max(end-1,0); ++s) {
					if(*s != '.' && !isdigit(*s)){
						d = atoi((char*)number.head);
						break;
					}
				}
			}
		}
		value += d;
		number.head = number.tail;
		number.tail = line->tail;
	}
	return value;
}

int add_gears(bstring* prev, bstring* line, bstring* next){
	int value = 0;
	bstring gear = *line;
	while (RE_matchp(bstring_c("\\*"), gear, &gear)) {
		// Gear valid if there are two nearby numbers
		size start = gear.head - line->head;
		size end   = line->tail - gear.tail;

		int n_matches = 0;
		int numbers[2] = {0,0};

		bstring* lines[3] = {prev, line, next};
		for(int i=0; i<3; ++i){
			if(lines[i]) {
				bstring search_space  = bstring_slice(*lines[i], max(start-4,0), min(4-end,0));
				bstring n = search_space;
				while(RE_matchp(bstring_c("\\d+"), n, &n)) {
					if(n_matches < 2 && n.head <= lines[i]->head+start+1 && n.tail >= lines[i]->tail-end-1){
						numbers[n_matches++] = atoi((char*)n.head);
					}
					n.head = n.tail;
					n.tail = search_space.tail;
				}
			}
		}

		if(n_matches == 2){
			value += numbers[0]*numbers[1];
		}
		gear.head = gear.tail;
		gear.tail = line->tail;
	}

	return value;
}


int main(int argc, char *argv[]) {
	FILE *file = fopen("data.txt", "r");

	int answer1 = 0;
	int answer2 = 0;

	bstring l1 = bstring_alloc(LINE_SIZE+2);
	bstring l2 = bstring_alloc(LINE_SIZE+2);
	bstring l3 = bstring_alloc(LINE_SIZE+2);
	bstring* lines[3] = {&l1,&l2,&l3};

	int ln = 0;
	while (read_next_line(file, lines[ln%3], LINE_SIZE+2)) {
		if(ln != 0){
			answer1 += add_symbols((ln==1) ? NULL : lines[(ln-2)%3], lines[(ln-1)%3], lines[ln%3]);
			answer2 += add_gears((ln==1) ? NULL : lines[(ln-2)%3], lines[(ln-1)%3], lines[ln%3]);
		}
		++ln;
	}
	answer1 += add_symbols(lines[(ln-2)%3], lines[(ln-1)%3], NULL);

	printf("%d\n", answer1);
	printf("%d\n", answer2);

	ASSERT(answer1 == 532331);
	ASSERT(answer2 == 82301120);

	fclose(file);
	free(l1.head);
	free(l2.head);
	free(l3.head);
}