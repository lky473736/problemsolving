/* 
  2023-2학기 가천대학교 학습공동체 : 팀 GPT (Gachon Programming Team)
  topic 4 - 주사위 게임 (임규연)
  */

/*
<주사위 게임>

GPT는 기나긴 추석 연휴로 심심해서 미쳐버릴 지경이다. 마침 규연이는 눈이 6개인 주사위 1개를 가지고 있다. 규연이는 GPT에게 주사위 게임을 제안한다.

게임 진행 방식은 아래와 같다.

0. 참여자 수 N과 루프넘버 P를 정한다. 

1. 컴퓨터는 주사위를 3번 던진다. (이때 참여자는 컴퓨터가 주사위를 던진 결과를 모른다.)

2. 각각 참여자들은 컴퓨터가 던져서 나온 3번의 결과의 주사위 눈 수의 합이 얼마 이상인지를 제출한다.

3. 컴퓨터가 주사위 결과를 공개하고, 주사위 눈 수의 합을 공개한다. 

4. 참여자들이 생각한 수가 주사위 눈 수의 합보다 크면 1점, 참여자가 생각한 수가 주사위 눈 수의 합이랑 같으면 2점, 참여자가 생각한 수가 주사위 눈 수의 합보다 작으면 0점을 부여한다. 점수 결과를 출력한다.

5. 루프넘버 P만큼 1~4를 반복한다. 이때 각 참여자들의 점수는 누적되어야 한다.

6. 1등이 어떤 참가자인지를 출력한다.

예시)

주사위 게임!
참여자 수 N과 루프넘버 P를 작성 (공백 구분)
>>> 3 2
첫번째 게임입니다. 컴퓨터가 주사위를 3번 던졌습니다!
1번 참여자 : 주사위 눈 수의 합을 유추해주세요.
>>> 12
2번 참여자 : 주사위 눈 수의 합을 유추해주세요.
>>> 10
3번 참여자 : 주사위 눈 수의 합을 유추해주세요.
>>> 13
주사위 결과 : 1 6 6
주사위 눈 수의 합 : 13
1번 참여자 점수 : 0
2번 참여자 점수 : 0
3번 참여자 점수 : 2
두번째 게임입니다. 컴퓨터가 주사위를 3번 던졌습니다!
1번 참여자 : 주사위 눈 수의 합을 유추해주세요.
>>> 16
2번 참여자 : 주사위 눈 수의 합을 유추해주세요.
>>> 12
3번 참여자 : 주사위 눈 수의 합을 유추해주세요.
>>> 7
주사위 결과 : 2 3 2
주사위 눈 수의 합 : 7
1번 참여자 점수 : 1
2번 참여자 점수 : 1
3번 참여자 점수 : 4

최종 점수
1번 참여자 점수 : 1
2번 참여자 점수 : 1
3번 참여자 점수 : 4
*/

// 배열 사용할 때 주의사항 : https://zitto15.tistory.com/48

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

int main() {
    int N, P, gamecount = 1;
    printf("주사위 게임\n");

    printf("참여자 수 N과 루프넘버 P를 입력 (공백 구분)\n");
    scanf("%d %d", &N, &P);

    int scorearr[N]; // 점수 배열 생성 (참여자 수에 맞게 크기 설정)

    // scorearr 배열 초기화
    for (int i = 0; i < N; i++) {
        scorearr[i] = 0;
    }

    while (gamecount <= P) {
        int guessarr[N]; // 유추한 값을 넣는 배열 (참여자 수에 맞게 크기 설정)
        srand(time(NULL));

        // 3부터 18까지의 난수 생성 (세 주사위의 눈 수의 합의 최소는 3, 최대는 18)
        int min = 3;
        int max = 18;
        int random_number = (rand() % (max - min + 1)) + min;

        printf("%d번째 게임입니다.\n", gamecount);
        printf("컴퓨터가 주사위를 3번 던졌습니다!\n");

        for (int k = 0; k < N; k++) // 인원수만큼 반복
        {
            int guess = 0;

            printf("%d번 참여자 : 주사위 눈 수의 합을 유추해주세요.\n", k + 1);
            scanf("%d", &guess);

            guessarr[k] = guess; // guessarr 배열에 k번 참여자가 유추한 값 넣기
        }

        printf("주사위 눈 수의 합 : %d\n", random_number);

        for (int x = 0; x < N; x++) {
            int score = 0;

            if (guessarr[x] < random_number) // 유추한 값이 합보다 작음
            {
                scorearr[x] += 0;
            } 
            
            else if (guessarr[x] > random_number) // 유추한 값이 합보다 큼
            {
                scorearr[x] += 1;
            } 
            
            else // 유추한 값이 합과 동일함
            {
                scorearr[x] += 2;
            }

            printf("%d번 참여자 점수 : %d\n", x + 1, scorearr[x]);
        }

        gamecount++;
    }

    printf("최종 결과 :\n");

    for (int y = 0; y < N; y++) // 최종 결과 출력
    {
        printf("%d번 참여자 최종 점수 : %d\n", y + 1, scorearr[y]);
    }

    return 0;
}

/* 아래는 처음 코드 작성한 원본 (배열의 component가 이상하게 출력되었음. 아마도 index error)

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

// 배열 사용할 때 주의사항 : https://zitto15.tistory.com/48

int main()
{
    int N, P, gamecount = 1;
    printf ("주사위 게임 \n");
    
    printf ("참여자 수 N과 루프넘버 P를 입력 (공백 구분)\n");
    scanf ("%d %d", &N, &P);
    
    int scorearr[N]; // 점수 배열 생성 (빈 배열 생성)
    
    while (gamecount <= P) 
    {
        int guessarr[N]; // 유추한 값을 넣는 배열 (빈 배열 생성)
        srand (time(NULL));
        
        // 3부터 18까지의 난수 생성 (세 주사위의 눈 수의 합의 최소는 3, 최대는 18)
        int min = 3;
        int max = 18;
        int random_number = (rand() % (max - min + 1)) + min;
        
        printf ("%d번째 게임입니다.\n", gamecount);
        printf ("컴퓨터가 주사위를 3번 던졌습니다!\n");
        
        for (int k = 0; k < N; k++) // 인원수만큼 반복
        {
            int guess = 0;

            printf("%d번 참여자 : 주사위 눈 수의 합을 유추해주세요.\n", k + 1);
            scanf("%d", &guess);

            guessarr[k] = guess; // guessarr 배열에 k번 참여자가 유추한 값 넣기
        }
        
        printf ("주사위 눈 수의 합 : %d\n", random_number);
        
        for (int x = 0; x < N; x++) {
            int score = 0;

            if (guessarr[x] < random_number) // 유추한 값이 합보다 작음
            {
                scorearr[x] += 0;
            } 
            
            else if (guessarr[x] > random_number) // 유추한 값이 합보다 큼
            {
                scorearr[x] += 1;
            } 
            
            else // 유추한 값이 합과 동일함
            {
                scorearr[x] += 2;
            }
            
            printf ("%d번 참여자 점수 : %d\n", x + 1, scorearr[x - 1]);
        }
        
        gamecount += 1;
    }
    
    printf ("최종 결과 : \n");
    
    for (int y = 1; y <= N; y++) // 최종 결과 출력 
    {
        printf ("%d번 참여자 최종 점수 : %d\n", y, scorearr[y - 1]);
    }
    
    return 0;
}
*/
