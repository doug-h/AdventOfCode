#pragma once

#include "types.h"

static int min(int a, int b){ return (a<b) ? a : b; }
static int max(int a, int b){ return (a>b) ? a : b; }


int char_to_int(char c) {return c - '0'; }

// Wrapper around fgets, placing the line into a sized string
// NOTE- strips newline characters
size read_next_line(FILE *file, bstring *line, size max_line_length) {
  char *_r = fgets((char*)line->head, (int)max_line_length, file);

  if (!_r) { return 0; }

  line->tail = line->head + strcspn((char*)line->head, "\n");
  return line->tail - line->head;
}