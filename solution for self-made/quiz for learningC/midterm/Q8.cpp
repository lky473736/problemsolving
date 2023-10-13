#include <stdio.h>

int sum(int N){
   int s =0;
   for (int i=1; i<N+1; i++){
       if(i%2==0){
       s+=i*2;
   } else{
       s+=i;}
       
   }
   return s;
}

int main()
{   
    int n;
    scanf("%d",&n);
    
    int result = sum(n); // sum 함수 호출
    printf("결과: %d\n", result);

    return 0;
}
