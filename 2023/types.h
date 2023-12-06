#pragma once

#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define ASSERT(c) if (!(c)) __builtin_trap()

typedef uint8_t u8;
typedef uint16_t u16;
typedef uint64_t u64;
typedef ptrdiff_t size;

// ==================== Sized String ====================
typedef struct {
  u8 *head;
  size len;
} sstring;

#define sstring_c(c)                                                             \
  (sstring) { (u8 *)c, (size)(sizeof(c) - 1) }

static bool sstring_equals(sstring a, sstring b) {
  return a.len == b.len && !memcmp(a.head, b.head, a.len);
}
static void sstring_print(sstring s) {
  // printf("%.*s", (size)sizeof(s), s); // Stops on \0
  for (int i = 0; i < s.len; ++i) {
    putchar(s.head[i]);
  }
}

// Goes from [i0,i1), like python list[i0:i1]
static sstring sstring_slice(sstring s, size i0 , size i1) {
  ASSERT(i0 >= 0 && i0 < s.len);
  ASSERT(i1 > 0 && i1 <= s.len);
  ASSERT(i0 < i1);

  sstring slice = {.head = s.head + i0, .len = i1 - i0};
  return slice;
}

// ==================== Arena ====================
typedef struct {
  u8 *base;
  size free;
  size used;
} arena;

void arena_clear(arena *a) {
  a->free += a->used;
  a->used = 0;
}
void arena_free(arena *a) {
  free(a->base);
  a->free = 0;
  a->used = 0;
}
// NOTE - look into alignment
u8 *arena_pushbytes(arena *a, size count) {
  ASSERT(count <= a->free);
  u8 *r = a->base + a->used;
  a->free -= count;
  a->used += count;
  return r;
}
#define arena_alloc(a, T, n) (T *)arena_push_bytes(a, sizeof(T) * n)
