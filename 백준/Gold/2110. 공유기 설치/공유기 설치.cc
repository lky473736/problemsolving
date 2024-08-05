#include <bits/stdc++.h>
using namespace std;

vector<long long> arr;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N, C;
    cin >> N >> C;
    
    arr.resize(N); // 배열 크기를 조정
    
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    
    sort(arr.begin(), arr.end()); // 배열을 정렬
    
    if (C == 2) {
        cout << arr[N-1] - arr[0] << '\n'; // 최대니깐 그냥 맨 마지막에서 첫번째 빼기
        return 0;
    }
 
    long long start = 1; // 최소 거리
    long long end = arr[N - 1] - arr[0]; // 최대 거리 (정렬된 배열의 첫 번째와 마지막 요소의 차이)
    long long mid = 0; // 중간거리
    long long temp = 0; // 이전집 
    long long distance = 0; // 거리
    
    int cnt = 0;
    
    while (start < end) {
        cnt = 1; 
        mid = (start + end + 1) / 2;
        temp = arr[0];
        
        for (int i = 1; i < N; i++) { // 첫 번째 요소는 이미 사용했으므로 i를 1로 설정
            distance = arr[i] - temp; // 거리
            
            if (distance >= mid) { // 이전집과 거리가 mid보다 클때 설치
                cnt++; // 늘리고
                temp = arr[i]; // 이전집 두기
            }
        }
        
        if (cnt >= C) {
            start = mid;
        } 
        
        else { 
            end = mid - 1;
        }
    }
    
    cout << start << '\n'; // 최종 결과 출력

    return 0;
}