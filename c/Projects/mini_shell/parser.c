#include <stdio.h>
#include <stdlib.h>
// PROJECT: Mini Shell — Parser
//
// Turns token stream into an AST (command pipeline tree).
//
// TODO 1: AST node types
//   typedef enum { NODE_CMD, NODE_PIPE, NODE_SEQ, NODE_BG } NodeType;
//   typedef struct ASTNode {
//       NodeType type;
//       char **argv;          // for NODE_CMD
//       int argc;
//       char *redir_in;       // filename for <
//       char *redir_out;      // filename for >
//       int redir_append;     // 1 if >>
//       struct ASTNode *left, *right;  // for NODE_PIPE, NODE_SEQ
//   } ASTNode;
//
// TODO 2: Recursive descent parser
//   ASTNode *parse(Token *tokens, int count);
//   // Grammar:
//   //   seq     → pipeline (';' pipeline)*
//   //   pipeline → command ('|' command)*
//   //   command  → WORD+ redir*
//   //   redir   → '<' WORD | '>' WORD | '>>' WORD
//
// TODO 3: AST pretty printer (for debugging)
//   void ast_print(ASTNode *node, int depth);
//
// TODO 4: AST free
//   void ast_free(ASTNode *node);

int parser_placeholder(void) { return 0; }
