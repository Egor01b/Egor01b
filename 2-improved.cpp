#include <stdio.h>
int sum_of_args(int* args_in, int arg_count)
{
  int sum = 0;

  for (int i = 0; i < arg_count; i++)
  {
    sum += args_in[i];
  }

  return sum;
}


int main() 
{
  int arr[] = { 2, 3, 4, 1 };
  printf("%d\n" , sum_of_args(arr, 4));
  return 0;
}
