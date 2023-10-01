/* 
  2023-2학기 가천대학교 학습공동체 : 팀 GPT (Gachon Programming Team)
  topic 2 - 특정 범위 안의 등차수열의 합 (임규연)
  */

/*
특정 범위에서의 등차수열의 합 계산기

user에게 정수인 등차, 정수인 첫째항, 자연수 n, 자연수 m을 입력받는다. (각 변수의 구분은 띄어쓰기로 한다.) m과 n을 항의 번호라 할 때, n + 1번째 항~ m번째 항의 합을 실수형으로 출력하시오. 
*/

#include <stdio.h>

int main(void) 
{
    int d, a1, nvalue, mvalue; // nvalue : n입력, mvalue : m입력
    double k;

    scanf("%d %d %d %d", &d, &a1, &nvalue, &mvalue);

    k = mvalue * (2 * a1 + (mvalue - 1) * d) / 2 - nvalue * (2 * a1 + (nvalue - 1) * d) / 2; 

    printf("%f", k);

    return 0;
}
