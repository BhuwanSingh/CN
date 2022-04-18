#include<stdio.h>
#include<unistd.h>

int main() {
    int pipefds[2];
    int returnstatus;
    char writemessages[2][20]={"CN Lab ", "Assignment 8"};
    char readmessage[20];
    returnstatus = pipe(pipefds);

    if (returnstatus == -1) {
        printf("Unable to create pipe\n");
        return 1;
    }

    printf("Writing to pipe - Message is %s\n", writemessages[0]);
    write(pipefds[1], writemessages[0], sizeof(writemessages[0]));

    read(pipefds[0], readmessage, sizeof(readmessage));
    printf("Reading from pipe – Message is %s\n", readmessage);
    printf("Writing to pipe - Message is %s\n", writemessages[1]);

    write(pipefds[1], writemessages[1], sizeof(writemessages[1]));
    read(pipefds[0], readmessage, sizeof(readmessage));
    printf("Reading from pipe – Message is %s\n", readmessage);
    
    return 0;
}