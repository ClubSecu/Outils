/*
    Author : Nomekrax
    Creation : 29/05/15
    Last Modification : 10/06/15
    Informations : 
        compile with : gcc -m32 getenvaddress.c -o getenvaddress
*/

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
