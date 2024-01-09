import java.util.Scanner;
public class task19 
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println ("Enter number");
    int n = sc.nextInt();
    for (int i = n; i >= 1; i--)
    {
      for (int j = 1; j < i; j++) 
      {
        System.out.print(" ");
      }
      for (int k = i; k <= n; k++) 
      {
        if (i > 1 && i < n - 1) 
        {
          if (k > i && k < n) 
          {
            System.out.print(" ");
          } else
            System.out.print(k);
        } else
          System.out.print(k);
      }
      System.out.println();
    }
  }
}
