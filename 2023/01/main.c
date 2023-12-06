#include "../fileutils.h"
#include "../types.h"

#define MAX_LINE_SIZE 128

static sstring digit_names[9] = {
    sstring_c("one"),   sstring_c("two"),   sstring_c("three"),
    sstring_c("four"),  sstring_c("five"),  sstring_c("six"),
    sstring_c("seven"), sstring_c("eight"), sstring_c("nine")};

bool is_digit(char c) { return (c >= '0' && c <= '9'); }

int char_to_int(char c) {
  ASSERT(is_digit(c));
  return c - '0';
}

int is_digitname(sstring line) {
  if (line.len < 3) {
    return 0;
  }

  for (int i = 0; i < 9; ++i) {
    sstring name = digit_names[i];
    if ((name.len <= line.len) && !memcmp(line.head, name.head, name.len)) {
      return i + 1;
    }
  }
  return 0;
}

int process_line(sstring line) {
  int value = 0;
  for (int i = 0; i < line.len; ++i) {
    char c = line.head[i];
    if (is_digit(c)) {
      value = 10 * char_to_int(c);
      break;
    }
    sstring slice = sstring_slice(line, i, line.len);
    int idx = is_digitname(slice);
    if (idx) {
      value = 10 * idx;
      break;
    }
  }
  for (int i = (int)line.len - 1; i >= 0; --i) {
    char c = line.head[i];
    if (is_digit(c)) {
      value += char_to_int(c);
      break;
    }
    sstring slice = sstring_slice(line, i, line.len);
    int idx = is_digitname(slice);
    if (idx) {
      value += idx;
      break;
    }
  }
  return value;
}

int main(int argc, char *argv[]) {
  ASSERT(argc > 1); // Provide input file

  {
    FILE *file = fopen(argv[1], "r");
    ASSERT(file); // File failed to open

    int value = 0;
    sstring line;
    line.head = calloc(MAX_LINE_SIZE, 1);
    ASSERT(line.head); // Failed to allocate string
    while (read_next_line(file, &line, MAX_LINE_SIZE)) {
      value += process_line(line);
    }

    free(line.head);
    printf("%i\n", value);
    fclose(file);
  }

  return 0;
}
