#include <bits/stdc++.h>
using namespace std;

int S[] = {1, 3, 2, 4, -1, -9, 10};

int partition (int low, int high) {
  int i, j;
  j = low; 
  
  for (i = low+1; i <= high; i++) {
    if (S[i] < S[j]) {
      int temp = S[i];
      S[i] = S[j];
      S[j] = temp;
    }
  }
  int temp = S[low];
  S[low] = S[j];
  S[j] = temp;
  
  return j;
}

void quickSort (int low, int high) {
  int pivot;
  
  if (low < high) {
    pivot = partition(low, high);
    quickSort(low, pivot-1);
    quickSort(pivot+1, high);
  }
}

int main() {
  quickSort(0, 6);
  for (int i = 0; i < 7; i++) { cout << S[i] << ' '; }
}
