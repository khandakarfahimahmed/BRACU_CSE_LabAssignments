import java.util.Scanner;
public class task06
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println ("Give imput");
    int n = sc.nextInt();
    for (int i = 1;i<=n;i++)
    {
      for (int p = 1;p<=i;p++)
      {
        System.out.print(p);
      }
      System.out.println();
    }
  }
}