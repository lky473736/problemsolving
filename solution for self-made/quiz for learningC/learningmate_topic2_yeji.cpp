/* 
  2023-2학기 가천대학교 학습공동체 : 팀 GPT (Gachon Programming Team)
  topic 2 - 환율 계산 프로그램 (정예지)
  */

/* 환율을 계산하는 프로그램 */
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main (void) {
  double rate; //원/달러 환율 
  double usd; // 달러화 
  int krw; // 원화는 정수형 변수로 선언
  
  printf("환율을 입력하시오: "); 
  1/ 입력 안내 메시지 
  scanf("%lf', &rate); // 사용자로부터 환율입력
  printf("원화 금액을 입력하시오: "); // 입력 안내 메시지 
  scanf("%d", 8krw);// 원화 금액 입력
  usd = krw / rate; // 달러화로 환산
  printf(”원화 %d원은 %. 21F달러입니다. n"”, krw, usd); // 계산 결과 출력, 달러화를 소수점 이하를 2자리로 표시
  return 0; //함수 결과값 반환
}
