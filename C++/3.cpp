#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> beadSort(vector<int>& arr) {
    if (arr.empty()) return arr;

    int maxVal = *max_element(arr.begin(), arr.end());
    int n = arr.size();

    // Создаем "абак" - матрицу бусин
    vector<vector<int>> beads(maxVal, vector<int>(n, 0));

    // Располагаем бусины на абаке
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < arr[i]; j++) {
            beads[j][i] = 1;
        }
    }

    // Моделируем падение бусин под действием гравитации
    for (int i = 0; i < maxVal; i++) {
        // Считаем количество бусин в каждом ряду
        int beadCount = 0;
        for (int j = 0; j < n; j++) {
            beadCount += beads[i][j];
        }

        // Опускаем бусины вниз
        for (int j = 0; j < n; j++) {
            if (j < beadCount) {
                beads[i][j] = 1;
            }
            else {
                beads[i][j] = 0;
            }
        }
    }

    // Восстанавливаем отсортированный массив
    vector<int> result(n, 0);
    for (int j = 0; j < n; j++) {
        int columnSum = 0;
        for (int i = 0; i < maxVal; i++) {
            columnSum += beads[i][j];
        }
        result[j] = columnSum;
    }

    return result;
}

int main() {
    vector<int> arr = { 3, 1, 4, 1, 5, 9, 2, 6 };
    cout << "Исходный массив: ";
    for (int num : arr) cout << num << " ";
    cout << endl;

    vector<int> sortedArr = beadSort(arr);
    cout << "Отсортированный массив: ";
    for (int num : sortedArr) cout << num << " ";
    cout << endl;

    return 0;
}