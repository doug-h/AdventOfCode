#include "regex.h"

// For proper regex this would be something smarter 
// (tree -> NFA -> DFA or whatever)
struct regex_t {
    bstring compiled_regex;
};

typedef enum {
    RE_ANYCHAR          = 20,  // .
    RE_ANYWORD          = 21,  // \w
    RE_ANYDIGIT         = 22,  // \d
    RE_ANYWHITESPACE    = 23,  // \s
    RE_NOTWORD          = 24,  // \W
    RE_NOTDIGIT         = 25,  // \D
    RE_NOTWHITESPACE    = 26,  // \S
} RE_ATOMTYPE;

static u8* matchhere(bstring regexp, bstring text);
static u8* matchsome(int c, bstring regexp, bstring text, int min, int max);
static int isword(int c) { return c == '_' || isalnum(c); }
static int charsmatch(int c, int r);


// Replace wildcards (. or \w etc.) with a single byte
regex_t* RE_compile(bstring t) {
    regex_t* out = calloc(sizeof(regex_t), 1);
    out->compiled_regex = bstring_alloc(bstring_len(t));

    bstring u = out->compiled_regex;
    while (t.head < t.tail){
        if(*t.head == '.'){
            *u.head++ = (u8)RE_ANYCHAR;
            ++t.head;
        }
        else if(t.tail-t.head > 1 && *t.head == '\\'){
            int type = -1;
            switch (t.head[1]){
                case 'w': {
                    type = RE_ANYWORD;
                } break;
                case 'd': {
                    type = RE_ANYDIGIT;
                } break;
                case 's': {
                    type = RE_ANYWHITESPACE;
                } break;
                case 'W': {
                    type = RE_NOTWORD;
                } break;
                case 'D': {
                    type = RE_NOTDIGIT;
                } break;
                case 'S': {
                    type = RE_NOTWHITESPACE;
                } break;
            }
            *u.head++ = (type != -1) ? (u8)type : t.head[1];
            t.head += 2;
        }
        else {
            *u.head++ = *t.head++;
        }
    }
    out->compiled_regex.tail = u.head;
    return out;
}

void RE_free(regex_t* creg){
    free(creg->compiled_regex.head);
    free(creg);
}
int RE_matchp(bstring pattern, bstring text, bstring* _match) {
    regex_t* re = RE_compile(pattern);
    int result = RE_matchc(re, text, _match);
    RE_free(re);
    return result;
}

// Walks through text until regexp accepts it
int RE_matchc(regex_t* re, bstring text, bstring* _match)
{
    bstring regexp = re->compiled_regex;
    bstring t = text;
    do {
        u8* end = matchhere(regexp, t);
        if (end){
            if(_match){
                *_match = (bstring){.head = t.head, .tail = end};
            }
            return 1;
        }
    } while (t.head++ < t.tail);

    // Ran out of text, no match
    return 0;
}

// Returns whether regexp accepts text
static u8* matchhere(bstring regexp, bstring text)
{
    if (regexp.head == regexp.tail){
        // Ran out of regex, we must have matched
        return text.head;
    }
    if(regexp.tail - regexp.head > 1) {

        if (regexp.head[1] == '*'){
            // Regex starts with c*, so we accept 0 or more c's
            regexp.head += 2;
            return matchsome(regexp.head[-2], regexp, text, 0, 0);
        }
        else if (regexp.head[1] == '+'){
            // Regex starts with c+, so we accept 1 or more c's
            regexp.head += 2;
            return matchsome(regexp.head[-2], regexp, text, 1, 0);
        }
        else if (regexp.head[1] == '?'){
            // Regex starts with c?, so we accept 0 or 1 c's
            regexp.head += 2;
            return matchsome(regexp.head[-2], regexp, text, 0, 1);
        }
    }
    if (text.head < text.tail && charsmatch(*text.head, *regexp.head)){
        // Step forward
        ++regexp.head;
        ++text.head;
        return matchhere(regexp, text);
    }
    return NULL;
}

static int charsmatch(int c, int r){
    return (r == c
        || (r == RE_ANYCHAR && c != '\n')
        || (r == RE_ANYWORD && isword(c)) 
        || (r == RE_ANYDIGIT && isdigit(c))
        || (r == RE_ANYWHITESPACE && isspace(c))
        || (r == RE_NOTWORD && !isword(c)) 
        || (r == RE_NOTDIGIT && !isdigit(c))
        || (r == RE_NOTWHITESPACE && !isspace(c))
    );
}
 
static u8* matchsome(int c, bstring regexp, bstring text, int min, int max)
{
    // Skip over a block of c's
    bstring t = text;
    while((t.head < t.tail) 
        && (max == 0 || t.head-text.head < max) 
        && charsmatch(*t.head, c)) {
        ++t.head;
    }
    
    // Walk back till we match the whole pattern
    while(t.head >= text.head+min) {
        u8* end = matchhere(regexp, t);
        if (end){
            return end;
        }
        --t.head;
    }
    return NULL;
}





void test_fullmatch(regex_t* creg, bstring text){
    bstring m;
    int i = RE_matchc(creg,text,&m);
    ASSERT(i && bstring_equals(m, text));
}
void test_match(regex_t* creg, bstring text, bstring result){
    bstring m;
    int i = RE_matchc(creg,text,&m);
    ASSERT(i && bstring_equals(m, result));
}
void test_nomatch(regex_t* creg, bstring text){
    ASSERT(!RE_matchc(creg,text,NULL));
}

void test(){
    bstring reg1 = bstring_c("a+b.\\d?c*");
    regex_t* creg1 = RE_compile(reg1);

    test_fullmatch(creg1, bstring_c("abx1"));
    test_fullmatch(creg1, bstring_c("aabx1"));

    test_nomatch(creg1, bstring_c("ab"));
    test_nomatch(creg1, bstring_c("a1"));
    test_nomatch(creg1, bstring_c("b1"));

    test_match(creg1, bstring_c("ooaxoabx"), bstring_c("abx"));
    test_match(creg1, bstring_c("ooaxoabx1"), bstring_c("abx1"));
    test_match(creg1, bstring_c("ooaxoabxuu"), bstring_c("abx"));

    RE_free(creg1);

    puts("Passed all tests!");
}