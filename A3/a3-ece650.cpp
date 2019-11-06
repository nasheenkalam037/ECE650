#include <stdio.h>
#include <iostream>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

using namespace std;

int main(int argc, char **argv)
{
  int pipergenop[2];
  pipe(pipergenop);

  pid_t child0_pid = fork();

  ///start rgen process

    if (child0_pid<0)
    {
        exit(EXIT_FAILURE);
    }

    else if (child0_pid == 0)
    {
        close(pipergenop[0]);
  		dup2(pipergenop[1], STDOUT_FILENO);
  		close(pipergenop[1]);
  		execvp("./rgen", argv);
        //execl("/bin/sh", "sh", "-c", , NULL);
    }

  close(pipergenop[1]);


  ///start process between rgen and A1

  int pipergenA1[2];
  pipe(pipergenA1);

  pid_t child1_pid= fork();

  if (child1_pid < 0)
  {
     exit(EXIT_FAILURE);
  }

  else if (child1_pid==0)
  {
    dup2(pipergenop[0], STDIN_FILENO);
    close(pipergenop[0]);
    close(pipergenA1[0]);
    dup2(pipergenA1[1], STDOUT_FILENO);
    close(pipergenA1[1]);
    execl("/bin/sh", "sh", "-c", "python ./a1-ece650.py",(char *) NULL);
  }


  close(pipergenop[0]);
  close(pipergenA1[1]);


  ///A2 process starts - receiving
  FILE* send_value_a2 = popen("./a2-ece650", "w");


   ///A2 Process functionality starts
  int child2_pid = fork();

  if (child2_pid<0)
  {
      exit(EXIT_FAILURE);
  }

  if (child2_pid == 0)
  {
    FILE* read_from_a1 = fdopen(pipergenA1[0],"r");
    char* line = NULL;
    size_t bytes = 0;

    while(getline(&line, &bytes, read_from_a1) != -1)
    {
        cout<<line;
        fputs(line, send_value_a2);
        fflush(send_value_a2);
    }

    fclose(read_from_a1);
    fclose(send_value_a2);
    exit(EXIT_SUCCESS);
  }

  close(pipergenA1[0]);

  char* line = NULL;
  size_t bytes = 0;

  while(getline(&line, &bytes, stdin) != -1)
  {
  	fputs(line, send_value_a2);
  	fflush(send_value_a2);
  }

  kill(child0_pid, SIGTERM);
  pclose(send_value_a2); //send EOF to a2
  return EXIT_SUCCESS;

  kill(child1_pid, SIGTERM);
  return EXIT_SUCCESS;

  kill(child2_pid, SIGTERM);
  return EXIT_SUCCESS;




}

