#include "../types.h"
#include "../utils.h"
#include "../regex.h"

#define LINE_SIZE 116
#define NUM_LINES 198

#define WINNING_NUMBERS 10
#define PLAYER_NUMBERS 25

int main(int argc, char *argv[]) {
	FILE *file = fopen("data.txt", "r");

	int answer1 = 0;
	int answer2 = 0;

	int num_tickets[NUM_LINES] = {0};

	bstring line_buffer = bstring_alloc(LINE_SIZE+2);

	int ticket_nums[1+WINNING_NUMBERS+PLAYER_NUMBERS];
	int ln = 0;
	while (read_next_line(file, &line_buffer, LINE_SIZE+2)) {
		bstring number = line_buffer;
		int ti = 0;
		while(RE_matchp(bstring_c("\\d+"), number, &number)){
			ticket_nums[ti++] = atoi((char*)number.head);

			number.head = number.tail;
			number.tail = line_buffer.tail;
		}
		int n_wins = 0;
		for(int i=0; i<PLAYER_NUMBERS; ++i){
			int pnum = ticket_nums[1+WINNING_NUMBERS+i];
			for(int j=0; j<WINNING_NUMBERS; ++j){
				if(pnum == ticket_nums[1+j])
				{
					++n_wins;
					break;
				}
			}
		}
		answer1 += (1 << (n_wins-1));
		answer2 += num_tickets[ln]+1;
		for(int i=0; i<n_wins; ++i){
			num_tickets[ln+i+1] += num_tickets[ln]+1;
		}
		++ln;
	}

	printf("%d\n", answer1);
	printf("%d\n", answer2);

	ASSERT(answer1 == 21138);
	ASSERT(answer2 == 7185540);

	fclose(file);
	free(line_buffer.head);
}