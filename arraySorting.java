package Sorting;

import java.util.Arrays;
import java.util.Scanner;

public class arraySorting {

    public static void main(String[] args)
    {
        int temp = 0;

        Scanner input = new Scanner(System.in);

        System.out.println("How many numbers do you want to sort? ");
        int sortNums = input.nextInt();

        int[] num = new int[sortNums];

        for(int i = 0; i < sortNums; i++)
        {
            System.out.println("Enter a number: ");
            num[i] = input.nextInt();
        }

        for(int i = 0; i < sortNums; i++)
        {
            for(int j = 0; j < sortNums; j++)
            {
                if(num[i] > num[j])
                {
                    temp = num[i];
                    num[i] = num[j];
                    num[j] = temp;
                }
            }
        }
        
        System.out.println(Arrays.toString(num));
    }
}