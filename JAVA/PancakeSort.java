public class PancakeSort {
    public static void pancakeSort(int[] arr) {
        int n = arr.length;

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

    private static void flip(int[] arr, int k) {
        int left = 0;
        while (left < k) {
            int temp = arr[left];
            arr[left] = arr[k];
            arr[k] = temp;
            left++;
            k--;
        }
    }

    public static void main(String[] args) {
        int[] arr = {23, 10, 20, 11, 12, 6, 7};
        System.out.print("Исходный массив: ");
        for (int num : arr) System.out.print(num + " ");
        System.out.println();

        int[] sortedArr = arr.clone();
        pancakeSort(sortedArr);
        System.out.print("Отсортированный массив: ");
        for (int num : sortedArr) System.out.print(num + " ");
        System.out.println();
    }
}