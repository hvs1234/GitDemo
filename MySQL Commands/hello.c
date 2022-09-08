#include<stdio.h>
#include<unistd.h>
int main()
{ //fork();
  if(fork() || fork()) {
  printf("\nhello1\n"); }
printf("\nhello2"); return 0; }

