import java.util.*;

public class BucketSort {
    public static double[] bucketSort(double[] arr) {
        if (arr.length == 0) return arr;

        int bucketCount = arr.length;
        double maxVal = Arrays.stream(arr).max().getAsDouble();
        double minVal = Arrays.stream(arr).min().getAsDouble();
        double bucketRange = (maxVal - minVal) / bucketCount;

        List<List<Double>> buckets = new ArrayList<>();
        for (int i = 0; i <= bucketCount; i++) {
            buckets.add(new ArrayList<>());
        }

        for (double num : arr) {
            int index = (int) ((num - minVal) / bucketRange);
            buckets.get(index).add(num);
        }

        List<Double> result = new ArrayList<>();
        for (List<Double> bucket : buckets) {
            insertionSort(bucket);
            result.addAll(bucket);
        }

        return result.stream().mapToDouble(Double::doubleValue).toArray();
    }

    private static void insertionSort(List<Double> arr) {
        for (int i = 1; i < arr.size(); i++) {
            double key = arr.get(i);
            int j = i - 1;
            while (j >= 0 && arr.get(j) > key) {
                arr.set(j + 1, arr.get(j));
                j--;
            }
            arr.set(j + 1, key);
        }
    }

    public static void main(String[] args) {
        double[] arr = {0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51};
        System.out.print("Исходный массив: ");
        for (double num : arr) System.out.print(num + " ");
        System.out.println();

        double[] sortedArr = bucketSort(arr);
        System.out.print("Отсортированный массив: ");
        for (double num : sortedArr) System.out.print(num + " ");
        System.out.println();
    }
}