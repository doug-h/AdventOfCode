#include <cstdio>
#include <cassert>
#include <cstring>

#include "input.h"

bool match(int index, int warp, const char *target, int target_len) {
  int start = index - warp;
  if (start < 0) { return false; }
  if (start + (target_len - 1) * warp >= (int)input_len) { return false; }

  for (int i = 0; i < target_len; ++i) {
    if (input[start + i * warp] != target[i]) { return false; }
  }
  return true;
}

int main(int argc, char *argv[]) {

  int w = strcspn(input, "\n") + 1;
  int warps[4] = {w + 1, w - 1, 1, w};

  int answer1 = 0, answer2 = 0;
  for (int i = 0; i < (int)input_len; ++i) {
    for (int warp : warps) {
      if (match(i, warp, "XMAS", 4) || match(i, warp, "SAMX", 4)) { ++answer1; }
    }

    if ((match(i, warps[0], "MAS", 3) || match(i, warps[0], "SAM", 3)) &&
        (match(i, warps[1], "MAS", 3) || match(i, warps[1], "SAM", 3))) {
      ++answer2;
    }
  }

  printf("%d, %d\n", answer1, answer2);
  return 0;
}
