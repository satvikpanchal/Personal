package Personal;

import java.util.Scanner;

public class palindrome
{
    public static void main(String[] args)
    {
        String str;

        StringBuilder sb = new StringBuilder();

        Scanner input = new Scanner(System.in);

        System.out.println("What string should I check?");
        str = input.nextLine();

        StringBuilder sb2 = new StringBuilder(str);

        char list[] = str.toCharArray();

        for(int i = (list.length - 1); i >= 0; i--)
        {
            sb.append(list[i]);
        }

        if(sb2.toString().equals(sb.toString()))
        {
            System.out.println(str + " is a palindrome.");
        }
        else
            System.out.println(str + " is not a palindrome.");
    }

}
