#include "../types.h"
#include "../utils.h"

#include <ctype.h>

static bstring digit_names[9] = {
    bstring_c("one"),   bstring_c("two"),   bstring_c("three"),
    bstring_c("four"),  bstring_c("five"),  bstring_c("six"),
    bstring_c("seven"), bstring_c("eight"), bstring_c("nine")};

int read_digit_name(bstring s) {
  for (int i = 0; i < 9; ++i) {
    bstring name = digit_names[i];
    if ((bstring_len(name) <= bstring_len(s)) &&
        !memcmp(s.head, name.head, bstring_len(name))) {
      return i + 1;
    }
  }
  return 0;
}

int find_value(bstring s, int part) {
  if (isdigit(s.head[0])) {
    return char_to_int(s.head[0]);
  }
  if (part == 2) {
    int d = read_digit_name(s);
    if (d) {
      return d;
    }
  }
  return -1;
}

int process_line(bstring line, int part) {
  int v1, v2;
  for (int i = 0; i < bstring_len(line); ++i) {
    v1 = find_value(bstring_slice(line, i, 0), part);
    if (v1 != -1) {
      break;
    }
  }
  for (int i = (int)bstring_len(line) - 1; i >= 0; --i) {
    v2 = find_value(bstring_slice(line, i, 0), part);
    if (v2 != -1) {
      break;
    }
  }
  return v1 * 10 + v2;
}

int main(int argc, char *argv[]) {

  FILE *file = fopen("data.txt", "r");
  ASSERT(file); // File failed to open
  int MAX_LINE_SIZE = 128;

  bstring line;
  line.head = (u8 *)calloc(MAX_LINE_SIZE, 1);
  ASSERT(line.head); // Failed to allocate string

  int answer1 = 0, answer2 = 0;
  while (read_next_line(file, &line, MAX_LINE_SIZE)) {
    answer1 += process_line(line, 1);
    answer2 += process_line(line, 2);
  }

  free(line.head);
  fclose(file);

  ASSERT(answer1 != 56506);
  printf("%i\n", answer1);
  ASSERT(answer2 == 56017);
  printf("%i\n", answer2);

  return 0;
}
