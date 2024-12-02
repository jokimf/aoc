package day3;

import helper.Parser;

import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

public class Day3 {

    public static void main(String[] args) throws IOException {
        Set<Coordinate> visited = new HashSet<>();

        String input = Parser.read("src/day3/data.txt").trim();

        var c = new Coordinate(0, 0);
        for (int i = 0; i < input.length(); i++) {
            char a = input.charAt(i);
            if (a == '>') {
                c.x++;
            } else if (a == '<') {
                c.x--;
            } else if (a == '^') {
                c.y++;
            } else if (a == 'v') {
                c.y--;
            } else {
                throw new IllegalArgumentException(String.valueOf(a));
            }
            visited.add(c);
        }
        System.out.println(visited.size());
    }

    public class Coordinate {
        public int x;
        public int y;

        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

}
