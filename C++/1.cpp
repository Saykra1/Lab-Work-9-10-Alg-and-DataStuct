#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void insertionSort(vector<double>& arr) {
    for (int i = 1; i < arr.size(); i++) {
        double key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

vector<double> bucketSort(vector<double>& arr) {
    if (arr.empty()) return arr;

    int bucketCount = arr.size();
    double maxVal = *max_element(arr.begin(), arr.end());
    double minVal = *min_element(arr.begin(), arr.end());
    double bucketRange = (maxVal - minVal) / bucketCount;

    vector<vector<double>> buckets(bucketCount + 1);

    for (double num : arr) {
        int index = (num - minVal) / bucketRange;
        buckets[index].push_back(num);
    }

    vector<double> result;
    for (auto& bucket : buckets) {
        insertionSort(bucket);
        result.insert(result.end(), bucket.begin(), bucket.end());
    }

    return result;
}

int main() {
    vector<double> arr = { 0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51 };
    cout << "Исходный массив: ";
    for (double num : arr) cout << num << " ";
    cout << endl;

    vector<double> sortedArr = bucketSort(arr);
    cout << "Отсортированный массив: ";
    for (double num : sortedArr) cout << num << " ";
    cout << endl;

    return 0;
}