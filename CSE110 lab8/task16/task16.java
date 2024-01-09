import java.util.Scanner;
public class task16
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println ("Enter number");
    int n = sc.nextInt();
    for (int i = 1; i <= n; i++) 
    {
      for (int j = 1; j <= i; j++)
      {
        if (i > 2 && i < n) {
          if (j > 1 && j < i)
            System.out.print(" ");
          else
            System.out.print("*");
        } else
          System.out.print("*");
      }
      System.out.println();
    }
    
  }
}
