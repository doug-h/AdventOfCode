#pragma once

#include "types.h"

#include <ctype.h>

/* RE 

taken from POSIX docs
+---+----------------------------------------------------------+
|   |             ERE Precedence (from high to low)            |
+---+----------------------------------------------------------+
| 1 | Collation-related bracket symbols | [==] [::] [..]       |
| 2 | Escaped characters                | \<special character> |
| 3 | Bracket expression                | []                   |
| 4 | Grouping                          | ()                   |
| 5 | Single-character-ERE duplication  | * + ? {m,n}          |
| 6 | Concatenation                     |                      |
| 7 | Anchoring                         | ^ $                  |
| 8 | Alternation                       | |                    |
+---+-----------------------------------+----------------------+
*/


typedef struct regex_t regex_t;

// Can either call RE_matchp with a regex pattern string, or compile the pattern once and use 
// it for multiple calls to RE_matchc
// Currently the compilation step just replaces some chars with bytes (e.g. \w -> RE_ANYWORD)
// so precompiling the pattern won't be noticably faster than just calling RE_matchp every time
int RE_matchp(bstring pattern, bstring text, bstring* match);
int RE_matchc(regex_t* re, bstring text, bstring* match);

regex_t* RE_compile(bstring pattern);
void RE_free(regex_t* re);
