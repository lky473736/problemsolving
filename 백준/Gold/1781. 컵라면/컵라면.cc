#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    
    vector<pair<int, int>> arr(N);
    
    for (int i = 0; i < N; i++) {
        int p, q;
        cin >> p >> q;
        
        arr[i].first = p;
        arr[i].second = q;
    }
    
    sort(arr.begin(), arr.end()); // deadline기준으로 오름차순
    
    priority_queue<int, vector<int>, greater<int>> p_que; // https://kbj96.tistory.com/15
    
    for (int i = 0; i < N; i++) {
		if (p_que.size() < arr[i].first) { // 여기서 p_que의 크기가 현재 시간을 의미
			p_que.push(arr[i].second); // 현재시간(큐 원소의 갯수) 보다 deadline이 작다면
		}
		
		else {
			if (p_que.top() < arr[i].second) { // 컵라면수랑 현재 컵라면수 비교할때 현재 컵라면이 더 크다면?
				p_que.pop(); // top 제거
				p_que.push(arr[i].second); // 넣기 (그니깐 위에있는게 현재 컵라면보다 작으면 손해니깐 최댓값을 구하기 위하여 이 과정을 하는 것)
			}
		}
	}
	
	int sumation = 0; // 지금 p_que에 있는 것들만 더하면 됨
	
	while (!p_que.empty())	{
		sumation += p_que.top();
		p_que.pop();
	}
	
	cout << sumation << '\n';
	
	return 0;
}