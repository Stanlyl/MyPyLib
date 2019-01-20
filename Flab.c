#include <stdlib.h>
#include <string.h>
int main(int argc,char *argv[])
{
	char comand[] = {"python "};
	char dot[] = {" "};
	int i;
	for(i=1;i<=argc;i++)
	{
		strcpy(comand, argv[i]);
		strcpy(comand, dot);
	}
	printf(comand);
	system(comand);
	return 0;
}