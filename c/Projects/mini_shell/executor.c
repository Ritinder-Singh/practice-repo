#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>
// PROJECT: Mini Shell — Executor & Main Entry Point
//
// TODO 1: Execute a single command (NODE_CMD)
//   void exec_cmd(ASTNode *node) {
//       pid_t pid = fork();
//       if (pid == 0) {
//           // child: set up redirections, execvp
//           if (node->redir_in) { int fd = open(node->redir_in, O_RDONLY); dup2(fd, 0); }
//           if (node->redir_out) { int fd = open(node->redir_out, O_WRONLY|O_CREAT|O_TRUNC, 0644); dup2(fd, 1); }
//           execvp(node->argv[0], node->argv);
//           perror(node->argv[0]); exit(127);
//       }
//       waitpid(pid, NULL, 0);  // parent waits
//   }
//
// TODO 2: Execute pipeline (NODE_PIPE)
//   // Create pipe(); fork twice; left child writes to pipe[1], right reads pipe[0]
//   int pfd[2]; pipe(pfd);
//
// TODO 3: Built-in commands
//   if (strcmp(argv[0], "cd") == 0) chdir(argv[1]);
//   if (strcmp(argv[0], "exit") == 0) exit(0);
//   if (strcmp(argv[0], "export") == 0) setenv(...);
//
// TODO 4: Main REPL
//   int main(void) {
//       char line[4096];
//       while (1) {
//           printf("$ "); fflush(stdout);
//           if (!fgets(line, sizeof(line), stdin)) break;
//           line[strcspn(line, "\n")] = '\0';
//           int count; Token *tokens = tokenize(line, &count);
//           ASTNode *ast = parse(tokens, count);
//           execute(ast);
//           ast_free(ast); tokens_free(tokens, count);
//       }
//   }
//
// TODO 5: Signal handling
//   signal(SIGINT, SIG_IGN);   // shell ignores Ctrl-C
//   signal(SIGCHLD, SIG_DFL);  // reap zombies

int main(void) {
    printf("Mini Shell — TODO: implement lexer.c, parser.c, then fill this out\n");
    return 0;
}
