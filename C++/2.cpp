#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void flip(vector<int>& arr, int k) {
    int left = 0;
    while (left < k) {
        swap(arr[left], arr[k]);
        left++;
        k--;
    }
}

void pancakeSort(vector<int>& arr) {
    int n = arr.size();

    for (int currSize = n; currSize > 1; currSize--) {
        // Находим индекс максимального элемента
        int maxIdx = 0;
        for (int i = 1; i < currSize; i++) {
            if (arr[i] > arr[maxIdx]) {
                maxIdx = i;
            }
        }

        if (maxIdx != currSize - 1) {
            // Переворачиваем до максимального элемента
            flip(arr, maxIdx);
            // Переворачиваем весь подмассив
            flip(arr, currSize - 1);
        }
    }
}

int main() {
    vector<int> arr = { 23, 10, 20, 11, 12, 6, 7 };
    cout << "Исходный массив: ";
    for (int num : arr) cout << num << " ";
    cout << endl;

    vector<int> sortedArr = arr;
    pancakeSort(sortedArr);
    cout << "Отсортированный массив: ";
    for (int num : sortedArr) cout << num << " ";
    cout << endl;

    return 0;
}