#pragma once

#include "types.h"

size read_next_line(FILE *file, sstring *line, size max_line_length) {
  char *_r = fgets((char*)line->head, (int)max_line_length, file);
  if (!_r) {
    return 0;
  }
  size len = strcspn((char*)line->head, "\n");
  line->head[len] = 0;

  line->len = len;
  return len;
}
