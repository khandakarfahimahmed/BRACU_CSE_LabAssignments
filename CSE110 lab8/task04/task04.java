import java.util.Scanner;
public class task04
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println ("Enter row");
    int r = sc.nextInt();
    System.out.println("Enter collumn");
    int c = sc.nextInt();
    for (int i = 1 ; i<=r;i++)
    {
      for (int p = 1; p<=c;p++)
        System.out.print(p);
      System.out.println();
    }
  }
}