#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    if(argc != 2){
        printf("Error");
        return 1;
    }
    printf("%p | %s\n",getenv(argv[1]), getenv(argv[1]));
}
