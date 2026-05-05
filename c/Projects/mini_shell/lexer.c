#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
// PROJECT: Mini Shell — Lexer
// Run: compile all three files: gcc -o minish lexer.c parser.c executor.c
//
// Tokenizes raw input line into a stream of tokens.
//
// TODO 1: Token types
//   typedef enum {
//       TOK_WORD,    // command name or argument
//       TOK_PIPE,    // |
//       TOK_REDIR_IN,  // <
//       TOK_REDIR_OUT, // >
//       TOK_REDIR_APPEND, // >>
//       TOK_SEMICOLON, // ;
//       TOK_BG,      // &
//       TOK_EOF,
//   } TokenType;
//   typedef struct { TokenType type; char *value; } Token;
//
// TODO 2: Lexer struct
//   typedef struct { const char *input; int pos; } Lexer;
//   Token lexer_next(Lexer *l);
//   // Skip whitespace; detect multi-char operators (>>, &&, ||)
//   // Handle single-quoted and double-quoted strings
//
// TODO 3: Tokenize function — return Token[]
//   Token *tokenize(const char *line, int *count);
//   // Allocate array; caller frees both the array and each token->value
//
// TODO 4: Free token list
//   void tokens_free(Token *tokens, int count);

int lexer_placeholder(void) { return 0; }
