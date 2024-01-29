#pragma once

#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <assert.h>

//#define ASSERT(c) if (!(c)) __builtin_trap()
#define ASSERT(c) assert(c)

typedef uint8_t u8;
typedef uint16_t u16;
typedef uint64_t u64;
typedef ptrdiff_t size;
// ptrdiff_t may be smaller than size_t, and would fail for veeerrry
// large arrays (>8 exabytes on my machine but may be smaller elsewhere)


// Trying out different string types to see what I like

// ==================== Sized String ====================
// Basically a fat pointer, could be null terminated too
typedef struct {
  u8 *head;
  size len;
} sstring;

#define sstring_c(c)                                                             \
  (sstring) { (u8 *)c, (size)(sizeof(c) - 1) }

// Allocate memory and return a sstring pointing at it
static sstring sstring_alloc(size len){
  sstring s =  {.head = (u8*)calloc(len, 1), .len=len};
  return s;
}

static bool sstring_equals(sstring a, sstring b) {
  return a.len == b.len && !memcmp(a.head, b.head, a.len);
}
static void sstring_print(sstring s) {
  printf("%.*s", (int)s.len, s.head);
}

// Goes from [i0,i1), e.g. python list[i0:i1]
static sstring sstring_slice(sstring s, size i0 , size i1) {
  ASSERT(i0 >= 0 && i0 < s.len);
  ASSERT(i1 > 0 && i1 <= s.len);
  ASSERT(i0 < i1);

  sstring slice = {.head = s.head + i0, .len = i1 - i0};
  return slice;
}

// ==================== Burger String ====================
// Tail points to one-past-the-end, so len = tail-head
typedef struct {
  u8 *head;
  u8 *tail;
} bstring;

static size bstring_len(bstring s){
  return s.tail-s.head;
}
#define bstring_c(c)                                                             \
  (bstring) { (u8 *)c, (u8*)(c+sizeof(c)-1) }

// Allocate memory and return a bstring pointing at it
static bstring bstring_alloc(size len){
  u8* d = (u8*)calloc(len, 1);
  return (bstring) {.head = d, .tail=d+len};
}
static bool bstring_equals(bstring a, bstring b) {
  return bstring_len(a) == bstring_len(b) && !memcmp(a.head, b.head, bstring_len(a));
}
static void bstring_print(bstring s) {
  printf("%.*s", (int)(s.tail-s.head), s.head);
}

// Goes from [i0,i1), a la python: L[i0:i1]
// i1==0 slices to the end
static bstring bstring_slice(bstring s, size i0 , size i1) {
  size len = bstring_len(s);
  i0 = (i0 <  0) ? i0 + len : i0;
  i1 = (i1 <= 0) ? i1 + len : i1;
  bstring slice = {.head = s.head + i0, .tail = s.head + i1};

  ASSERT(slice.head <= slice.tail);
  ASSERT(slice.head >= s.head);
  ASSERT(slice.tail <= s.tail);
  return slice;
}

// ==================== Arena ====================
typedef struct {
  u8 *base;
  size free;
  size used;
} arena;

static void arena_clear(arena *a) {
  a->free += a->used;
  a->used = 0;
}
static void arena_free(arena *a) {
  free(a->base);
  a->free = 0;
  a->used = 0;
}
// NOTE - look into alignment
static u8 *arena_pushbytes(arena *a, size count) {
  ASSERT(count <= a->free);
  u8 *r = a->base + a->used;
  a->free -= count;
  a->used += count;
  return r;
}
#define arena_alloc(a, T, n) (T *)arena_push_bytes(a, sizeof(T) * n)
