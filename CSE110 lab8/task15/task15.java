import java.util.Scanner;
public class task15
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println ("Enter row");
    int r = sc.nextInt();
    System.out.println("Enter collumn");
    int c = sc.nextInt();
    for (int i = 1; i <= r; i++)
    {
      for (int j = 1; j <= c; j++)
      {
        if (i == 1 || i == r) {
          System.out.print(j);
        } else if (j > 1 && j < c) {
          System.out.print(" ");
        } else
          System.out.print(j);
      }
      System.out.println();
    }
  }
}
