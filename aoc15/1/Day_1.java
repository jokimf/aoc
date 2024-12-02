package day1;

import helper.Parser;

import java.io.IOException;

public class Day_1 {

    public static void main(String[] args) throws IOException {
        String input = Parser.read("src/day1/data1.txt");

        int running = 0;
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (c == '(') {
                running++;
            } else if (c == ')') {
                running--;
            }
        }
        System.out.println(running);
    }
}
