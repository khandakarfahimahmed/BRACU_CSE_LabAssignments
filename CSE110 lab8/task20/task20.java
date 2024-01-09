import java.util.Scanner;
public class task20
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println ("Enter number");
    int n = sc.nextInt();
    for (int i = 0; i < n; i++) 
    {
      for (int j = i; j < n - 1; j++) 
      {
        System.out.print(" ");
      }
      
      for (int k = 1; k <= ((2 * i) + 1); k++)
      { 
        if (i > 0 && i < n - 1)
        {
          if (k > 1 && k < 2 * i + 1) 
          {
            System.out.print(" ");
          } else
            System.out.print("*");
        } else
          System.out.print("*");
      }
      System.out.println();
    }
  }
}
