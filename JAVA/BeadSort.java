import java.util.*;

public class BeadSort {
    public static int[] beadSort(int[] arr) {
        if (arr.length == 0) return arr;

        int maxVal = Arrays.stream(arr).max().getAsInt();
        int n = arr.length;

        // Создаем "абак" - матрицу бусин
        int[][] beads = new int[maxVal][n];

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
                } else {
                    beads[i][j] = 0;
                }
            }
        }

        // Восстанавливаем отсортированный массив
        int[] result = new int[n];
        for (int j = 0; j < n; j++) {
            int columnSum = 0;
            for (int i = 0; i < maxVal; i++) {
                columnSum += beads[i][j];
            }
            result[j] = columnSum;
        }

        return result;
    }

    public static void main(String[] args) {
        int[] arr = {3, 1, 4, 1, 5, 9, 2, 6};
        System.out.print("Исходный массив: ");
        for (int num : arr) System.out.print(num + " ");
        System.out.println();

        int[] sortedArr = beadSort(arr);
        System.out.print("Отсортированный массив: ");
        for (int num : sortedArr) System.out.print(num + " ");
        System.out.println();
    }
}