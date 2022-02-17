package Personal;

import java.util.Scanner;

public class Matrices {

    public static void main(String[] args)
    {
        int row;
        int column;

        Scanner input = new Scanner(System.in);

        System.out.println("How many rows do you want in the array?");
        row = input.nextInt();

        System.out.println("How many columns do you want in the array?");
        column = input.nextInt();

        int final_list[][] = new int[row][column];

        int list1[][] = new int[row][column];

        int list2[][] = new int[row][column];

        for(int i = 0; i < final_list.length; i++)
        {
            for(int j = 0; j < final_list[i].length; j++)
            {
             System.out.println("Enter numbers for the first matrix: ");
             list1[i][j] = input.nextInt();
            }
        }

        for(int i = 0; i < final_list.length; i++)
        {
            for(int j = 0; j < final_list[i].length; j++)
            {
                System.out.println("Enter numbers for the second matrix: ");
                list2[i][j] = input.nextInt();
            }
        }

        System.out.println();
        System.out.println("Addition");
        System.out.println();
        for(int i = 0; i < final_list.length; i++) {
            for (int j = 0; j < final_list[i].length; j++) {
                final_list[i][j] = list1[i][j] + list2[i][j];

                System.out.print(final_list[i][j] + " ");
            }
            System.out.println(" ");
        }

        System.out.println();
        System.out.println("Subtraction");
        System.out.println();
        for(int i = 0; i < final_list.length; i++)
        {
            for(int j = 0; j < final_list[i].length; j++)
            {
                final_list[i][j] = list1[i][j] - list2[i][j];

                System.out.print(final_list[i][j] + " ");
            }
            System.out.println(" ");
        }

        System.out.println();
        System.out.println("Multiplication");
        System.out.println();
        for(int i = 0; i < final_list.length; i++)
        {
            for(int j = 0; j < final_list[i].length; j++)
            {
                final_list[i][j] = list1[i][j] * list2[i][j];

                System.out.print(final_list[i][j] + " ");
            }
            System.out.println(" ");
        }
    }
}