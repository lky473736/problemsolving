#include <stdio.h>

int main() {
    int total_black_area = 0;

    // 도화지 크기
    int canvas_size = 100;

    // 흰 도화지 초기화
    int white_canvas[100][100] = {0};

    for (int k = 0; k < 2; k++) {
        int x, y;
        scanf("%d %d", &x, &y);

        // 종이의 왼쪽 위 모서리 좌표를 계산
        int left = x;
        int top = canvas_size - y - 10;

        // 영역을 1로 채움
        for (int i = top; i < top + 5; i++) {
            for (int j = left; j < left + 2; j++) {
                white_canvas[i][j] = 1;
            }
        }
    }

    // 흰 도화지에서 영역의 넓이를 계산
    for (int i = 0; i < canvas_size; i++) {
        for (int j = 0; j < canvas_size; j++) {
            if (white_canvas[i][j] == 1) {
                total_black_area += 1;
            }
        }
    }

    printf("%d\n", total_black_area);
    return 0;
}
