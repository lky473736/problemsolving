/* 
  2023-2학기 가천대학교 학습공동체 : 팀 GPT (Gachon Programming Team)
  topic 4 - 오름차순 정렬 : 버블 정렬 (한은진) 
  */

#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    int arr[100];
    
    int N, compo;
    
    int p, j;
   
    scanf ("%d", &N);
    
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &compo);
        arr[i] = compo;
    }
    
    for (p = 0; p < N; p++)
    {
        for (j = 0; j < N; j++)
        {
            if (p == j) 
            {
                ;
            }
            
            else if (arr[p] < arr[j])
            {
                int temp = arr[p];
                arr[p] = arr[j];
                arr[j] = temp;
            }
        }
    }
    
    for (int count = 0; count < N; count++)
    {
        printf ("%d ", arr[count]);
    }
    
    return 0;
}
