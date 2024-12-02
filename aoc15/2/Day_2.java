package day2;

import helper.Parser;

import java.io.IOException;

public class Day_2 {

    public static void main(String[] args) throws IOException {
        String input = Parser.read("src/day2/data.txt");
        String[] a = input.split("\n");

        int sum = 0;
        for (String row : a) {
            int[] intValues = new int[3];
            String[] stringValues = row.split("x");
            int smallest = Integer.MAX_VALUE, second_smallest = Integer.MAX_VALUE;
            for (int i = 0; i < stringValues.length; i++) {
                var cleanedString = stringValues[i].replaceAll("\n", "").trim();
                intValues[i] = Integer.parseInt(cleanedString);
                if (intValues[i] < second_smallest) {
                    if (intValues[i] < smallest) {
                        second_smallest = smallest;
                        smallest = intValues[i];
                    } else {
                        second_smallest = intValues[i];
                    }
                }
            }
            int surface = smallest * second_smallest + (2 * intValues[0] * intValues[1] + 2 * intValues[1] * intValues[2] + 2 * intValues[0] * intValues[2]);
            sum += surface;
        }
        System.out.println(sum);
    }
}
